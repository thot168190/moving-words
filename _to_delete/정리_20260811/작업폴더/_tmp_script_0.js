
    // 정적 학습장 주소를 직접 열어 로그인 확인을 우회하지 못하도록 앱의 학습 진입점으로 보냅니다.
    if(window===window.top)window.location.replace('/#learn');
  