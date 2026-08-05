// ============================================================
// AuthContext — Firebase Authentication React Context
// ============================================================
// 사용자 인증 상태를 앱 전체에서 관리하는 Context Provider
//
// 사용법:
// 1. main.tsx에서 <AuthProvider>로 앱을 감싸기
// 2. 컴포넌트에서 useAuth() 훅으로 사용자 정보 접근
// ============================================================

import {
  createContext,
  useContext,
  useEffect,
  useState,
  type ReactNode,
} from 'react';
import {
  onAuthStateChanged,
  signInWithPopup,
  signInWithEmailAndPassword,
  createUserWithEmailAndPassword,
  sendPasswordResetEmail,
  signOut as firebaseSignOut,
  GoogleAuthProvider,
  OAuthProvider,
  type User,
} from 'firebase/auth';
import { auth } from '../lib/firebase';
import {
  createUserProfile,
  getUserProfile,
  deleteUserProfile,
  updateLearningProgress,
  EMPTY_LEARNING_PROGRESS,
  type LearningProgress,
  type UserProfile,
} from '../lib/firestore';

const LOCAL_PROGRESS_KEY = 'inkword_learning_progress';

// ── Context type ──

interface AuthContextType {
  user: User | null;
  profile: UserProfile | null;
  learningProgress: LearningProgress;
  loading: boolean;
  error: string | null;

  // Auth methods
  signInWithGoogle: () => Promise<void>;
  signInWithApple: () => Promise<void>;
  signInWithEmail: (email: string, password: string) => Promise<void>;
  signUpWithEmail: (email: string, password: string) => Promise<void>;
  sendPasswordReset: (email: string) => Promise<void>;
  deleteAccount: () => Promise<void>;
  signOut: () => Promise<void>;
  clearError: () => void;
  recordSceneCompletion: (sceneId: string, wordIds?: string[]) => Promise<void>;
}

const AuthContext = createContext<AuthContextType | null>(null);

// ── Provider component ──

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [profile, setProfile] = useState<UserProfile | null>(null);
  const [learningProgress, setLearningProgress] = useState<LearningProgress>(EMPTY_LEARNING_PROGRESS);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // Listen to auth state changes
  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, async (firebaseUser) => {
      setUser(firebaseUser);

      if (firebaseUser) {
        // Fetch or create user profile in Firestore
        try {
          let userProfile = await getUserProfile(firebaseUser.uid);
          if (!userProfile) {
            await createUserProfile(firebaseUser.uid, {
              email: firebaseUser.email,
              displayName: firebaseUser.displayName,
              photoURL: firebaseUser.photoURL,
            });
            userProfile = await getUserProfile(firebaseUser.uid);
          }
          setProfile(userProfile);

          // 비로그인 체험 기록이 있으면 로그인 즉시 계정 기록에 병합합니다.
          let localProgress: LearningProgress | null = null;
          try {
            const raw = localStorage.getItem(LOCAL_PROGRESS_KEY);
            localProgress = raw ? JSON.parse(raw) : null;
          } catch {
            localProgress = null;
          }

          const saved = userProfile?.learningProgress || EMPTY_LEARNING_PROGRESS;
          const merged: LearningProgress = {
            completedSceneIds: [...new Set([...(saved.completedSceneIds || []), ...(localProgress?.completedSceneIds || [])])],
            learnedWordIds: [...new Set([...(saved.learnedWordIds || []), ...(localProgress?.learnedWordIds || [])])],
            collectedCardIds: [...new Set([...(saved.collectedCardIds || []), ...(localProgress?.collectedCardIds || [])])],
            lastSceneId: localProgress?.lastSceneId || saved.lastSceneId || null,
            lastStudiedAt: localProgress?.lastStudiedAt || saved.lastStudiedAt || null,
          };
          setLearningProgress(merged);
          localStorage.setItem(LOCAL_PROGRESS_KEY, JSON.stringify(merged));
          if (localProgress) await updateLearningProgress(firebaseUser.uid, merged);
        } catch (err: any) {
          console.error('Failed to fetch user profile:', err);
          setError('데이터베이스(Firestore) 연결에 실패했습니다. Firebase 콘솔에서 Firestore Database 활성화 및 보안 규칙을 확인해 주세요.');
          setProfile(null);
        }
      } else {
        setProfile(null);
        try {
          const raw = localStorage.getItem(LOCAL_PROGRESS_KEY);
          setLearningProgress(raw ? JSON.parse(raw) : EMPTY_LEARNING_PROGRESS);
        } catch {
          setLearningProgress(EMPTY_LEARNING_PROGRESS);
        }
      }

      setLoading(false);
    });

    return () => unsubscribe();
  }, []);

  // ── Sign-in methods ──

  // ── Friendly Error Translator ──
  const getFriendlyErrorMessage = (err: any): string => {
    const code = err?.code || '';
    switch (code) {
      case 'auth/email-already-in-use':
        return '이미 가입된 이메일입니다. 로그인 화면에서 로그인을 진행해 주세요.';
      case 'auth/weak-password':
        return '비밀번호가 너무 취약합니다. 최소 6자 이상으로 설정해 주세요.';
      case 'auth/invalid-email':
        return '이메일 주소 형식이 올바르지 않습니다.';
      case 'auth/user-not-found':
      case 'auth/wrong-password':
      case 'auth/invalid-credential':
        return '가입되지 않은 이메일이거나, 비밀번호가 일치하지 않습니다.';
      case 'auth/too-many-requests':
        return '로그인 시도가 너무 많아 일시적으로 계정이 차단되었습니다. 잠시 후 다시 시도해 주세요.';
      default:
        return err.message || '인증 처리 중 오류가 발생했습니다. 다시 시도해 주세요.';
    }
  };

  // ── Sign-in methods ──

  const signInWithGoogle = async () => {
    try {
      setError(null);
      const provider = new GoogleAuthProvider();
      await signInWithPopup(auth, provider);
    } catch (err: any) {
      setError(getFriendlyErrorMessage(err));
      throw err;
    }
  };

  const signInWithApple = async () => {
    try {
      setError(null);
      const provider = new OAuthProvider('apple.com');
      await signInWithPopup(auth, provider);
    } catch (err: any) {
      setError(getFriendlyErrorMessage(err));
      throw err;
    }
  };

  const signInWithEmail = async (email: string, password: string) => {
    try {
      setError(null);
      await signInWithEmailAndPassword(auth, email, password);
    } catch (err: any) {
      setError(getFriendlyErrorMessage(err));
      throw err;
    }
  };

  const signUpWithEmail = async (email: string, password: string) => {
    try {
      setError(null);
      await createUserWithEmailAndPassword(auth, email, password);
    } catch (err: any) {
      setError(getFriendlyErrorMessage(err));
      throw err;
    }
  };

  const sendPasswordReset = async (email: string) => {
    try {
      setError(null);
      await sendPasswordResetEmail(auth, email);
    } catch (err: any) {
      setError(getFriendlyErrorMessage(err));
      throw err;
    }
  };

  const deleteAccount = async () => {
    const currentUser = auth.currentUser;
    if (!currentUser) throw new Error('로그인된 사용자가 없습니다.');
    try {
      setError(null);
      // 1. Firestore 프로필 삭제
      await deleteUserProfile(currentUser.uid);
      // 2. Firebase Auth 계정 완전 삭제
      await currentUser.delete();
    } catch (err: any) {
      setError(getFriendlyErrorMessage(err));
      throw err;
    }
  };

  const signOut = async () => {
    try {
      await firebaseSignOut(auth);
    } catch (err: any) {
      setError(getFriendlyErrorMessage(err));
    }
  };

  const clearError = () => setError(null);

  const recordSceneCompletion = async (sceneId: string, wordIds: string[] = []) => {
    const next: LearningProgress = {
      completedSceneIds: [...new Set([...learningProgress.completedSceneIds, sceneId])],
      learnedWordIds: [...new Set([...learningProgress.learnedWordIds, ...wordIds])],
      collectedCardIds: [...new Set([...learningProgress.collectedCardIds, sceneId])],
      lastSceneId: sceneId,
      lastStudiedAt: new Date().toISOString(),
    };
    setLearningProgress(next);
    localStorage.setItem(LOCAL_PROGRESS_KEY, JSON.stringify(next));
    if (user) await updateLearningProgress(user.uid, next);
  };

  return (
    <AuthContext.Provider
      value={{
        user,
        profile,
        learningProgress,
        loading,
        error,
        signInWithGoogle,
        signInWithApple,
        signInWithEmail,
        signUpWithEmail,
        sendPasswordReset,
        deleteAccount,
        signOut,
        clearError,
        recordSceneCompletion,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
}

// ── Hook ──

export function useAuth(): AuthContextType {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
}
