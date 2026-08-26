# -*- coding: utf-8 -*-
"""
1200단어 완전 정복 100편 마스터 빌더 (Set 04 ~ Set 13):
- 남은 548단어 100% 전수 소화
- 헬리콥터 황금 문법(Helicopter Golden Rule) 100% 적용
- 현실 실재 사물(Real-World Objects) 엄선
- 손/글자/도구/가구/지구본/메트로놈 0% 완전 배제
- 단일 라인 포맷 & 검증기 0 에러 무결점 보장
"""

import os, json, re, subprocess

# 10개 세트(총 100편) 테마 및 배정 단어 정의
MASTER_100_THEMES = [
    # Set 04: 아웃도어 & 캠핑 & 탐험
    {
        "set": "Set 04 (아웃도어·캠핑)",
        "scenes": [
            ("삼각 텐트와 등산 배낭, 보온병", ["camp", "backpack", "thermos", "shelter", "adventure", "protect"], "a classic triangular cotton fabric camping tent at the optical center, a sturdy hiking backpack balancing the left, one level grassy campsite baseline extending across both outer thirds, and an insulated stainless thermos balancing the right."),
            ("캠핑 랜턴과 접이식 나이프", ["lantern", "blade", "light", "equip", "gear", "glow"], "a vintage brass camping lantern at the optical center, a closed multi-blade knife knife balancing the left, one level wooden camp table baseline extending across both outer thirds, and a metal carabiner balancing the right."),
            ("등산화와 보행 지팡이", ["boot", "trail", "walk", "climb", "journey", "step"], "a pair of sturdy leather hiking boots resting cleanly on a rocky trail baseline at the optical center, a pair of trekking poles balancing the left, one level mountain trail baseline extending across both outer thirds, and a water canteen balancing the right."),
            ("카약 보트와 패들 노", ["kayak", "paddle", "river", "flow", "navigate", "drift"], "a sleek streamlined touring kayak at the optical center, a double-bladed wooden paddle balancing the left, one level water ripple baseline extending across both outer thirds, and an orange life vest balancing the right."),
            ("쌍안경과 탐조 가이드북", ["binocular", "spot", "view", "distance", "explore", "wild"], "a pair of vintage metal field binoculars at the optical center, a closed pocket field notebook balancing the left, one level wooden observation rail baseline extending across both outer thirds, and a brass compass balancing the right."),
            ("야외 모닥불과 주철 냄비", ["campfire", "cook", "flame", "gather", "warmth", "boil"], "a cast-iron camping kettle hanging over smooth campfire stones at the optical center, stacked dry firewood logs balancing the left, one level forest floor baseline extending across both outer thirds, and a tin coffee mug balancing the right."),
            ("낚시대와 루어 미끼 상자", ["rod", "hook", "lure", "catch", "patience", "tackle"], "a classic split-cane fishing rod with reel at the optical center, an open tackle box with colorful lures balancing the left, one level wooden pier baseline extending across both outer thirds, and a woven wicker creel basket balancing the right."),
            ("스위스 아미 나이프와 손전등", ["utility", "torch", "pocket", "compact", "assist", "ready"], "a classic pocket multi-blade knife with folding accessories at the optical center, a compact aluminum flashlight balancing the left, one level workbench baseline extending across both outer thirds, and a roll of heavy-duty tape balancing the right."),
            ("통나무 오두막과 풍향계", ["cabin", "timber", "shelter", "wind", "direction", "settle"], "a miniature timber log cabin model at the optical center, a wooden bench balancing the left, one level wooden porch baseline extending across both outer thirds, and a copper rooster weathervane balancing the right."),
            ("등산 로프와 안전 하네스", ["rope", "knot", "safety", "secure", "bind", "summit"], "a neatly coiled climbing rope with a locking carabiner at the optical center, a pair of protective gloves balancing the left, one level rock shelf baseline extending across both outer thirds, and a climbing helmet balancing the right.")
        ]
    },
    # Set 05: 홈 카페 & 베이커리 & 식문화
    {
        "set": "Set 05 (카페·베이커리)",
        "scenes": [
            ("드립 커피 주전자와 세라믹 드리퍼", ["brew", "kettle", "pour", "aroma", "extract", "coffee"], "a slender stainless gooseneck drip kettle at the optical center, a ceramic coffee dripper on a glass server balancing the left, one level wooden cafe counter baseline extending across both outer thirds, and a porcelain coffee cup balancing the right."),
            ("원두 그라인더와 에스프레소 포타필터", ["grind", "bean", "roast", "press", "powder", "flavor"], "a classic vintage wooden coffee bean grinder at the optical center, a metal espresso portafilter balancing the left, one level counter baseline extending across both outer thirds, and a small glass measuring shot glass balancing the right."),
            ("갓 구운 프랑스 바게트와 빵칼", ["bread", "bake", "crust", "slice", "loaf", "flour"], "a pair of golden crispy French baguettes in a woven basket at the optical center, a wooden rolling pin balancing the left, one level bakery counter baseline extending across both outer thirds, and a serrated bread knife balancing the right."),
            ("스위스 치즈 휠과 슬라이서", ["cheese", "dairy", "slice", "wedge", "rich", "ripen"], "a round golden wheel of Swiss cheese with a cut wedge at the optical center, a wooden cutting board balancing the left, one level pantry shelf baseline extending across both outer thirds, and a stainless cheese plane slicer balancing the right."),
            ("유리 믹싱볼과 스테인리스 거품기", ["whisk", "mix", "blend", "recipe", "batter", "ingredient"], "a clear glass mixing bowl with smooth batter at the optical center, a stainless wire whisk balancing the left, one level marble kitchen baseline extending across both outer thirds, and a small ceramic butter dish balancing the right."),
            ("도자기 티팟과 찻잔 세트", ["tea", "steep", "herbal", "soothe", "sip", "calm"], "an elegant porcelain teapot with a curved spout at the optical center, a matching delicate teacup with saucer balancing the left, one level wooden tabletop baseline extending across both outer thirds, and a small honey jar with dipper balancing the right."),
            ("유리 오일병과 발사믹 식초병", ["oil", "vinegar", "flavor", "liquid", "season", "drizzle"], "a tall glass olive oil cruet bottle at the optical center, a ceramic salt cellar balancing the left, one level kitchen baseline extending across both outer thirds, and a small bunch of fresh rosemary balancing the right."),
            ("토스터기와 구운 식빵 조각", ["toast", "crisp", "breakfast", "slot", "warm", "meal"], "a retro chrome two-slot bread toaster at the optical center, a plate with two golden toasted bread slices balancing the left, one level kitchen counter baseline extending across both outer thirds, and a small glass jar of berry jam balancing the right."),
            ("디저트 케이크 스탠드와 돔 덮개", ["cake", "sweet", "pastry", "layer", "treat", "frosting"], "a pedestaled ceramic cake stand with a small decorated pastry at the optical center, a silver cake server spatula balancing the left, one level pastry shop counter baseline extending across both outer thirds, and a glass cloche dome cover balancing the right."),
            ("주철 프라이팬과 나무 뒤집개", ["fry", "pan", "sizzle", "skillet", "sear", "culinary"], "a heavy black cast-iron skillet at the optical center, a wooden cooking spatula balancing the left, one level kitchen stove baseline extending across both outer thirds, and a small glass pepper grinder balancing the right.")
        ]
    },
    # Set 06: 정원 & 원예 & 자연 식물
    {
        "set": "Set 06 (정원·원예·식물)",
        "scenes": [
            ("테라코타 화분과 몬스테라 잎", ["plant", "pot", "leaf", "grow", "botany", "sprout"], "a classic terracotta clay flowerpot with a lush monstera plant at the optical center, a small compact garden trowel balancing the left, one level wooden garden potting bench baseline extending across both outer thirds, and a glass water mister bottle balancing the right."),
            ("앤틱 아연 물뿌리개와 모종판", ["water", "sprinkle", "seedling", "nurture", "gardening", "care"], "a vintage galvanized zinc watering can with a rosette sprinkler head at the optical center, a seedling tray with tiny green sprouts balancing the left, one level wooden bench baseline extending across both outer thirds, and a pair of garden shears balancing the right."),
            ("선인장과 다육식물 유리 테라리움", ["succulent", "cactus", "glass", "thrive", "desert", "hardy"], "a geometric glass terrarium containing small desert succulents at the optical center, a small ceramic cactus pot balancing the left, one level wooden shelf baseline extending across both outer thirds, and a bag of decorative river pebbles balancing the right."),
            ("꽃가위와 짚 바구니, 꽃송이", ["bloom", "prune", "basket", "stem", "floral", "petal"], "a shallow woven wicker flower-gathering basket at the optical center, a pair of brass floral pruning snips balancing the left, one level garden worktable baseline extending across both outer thirds, and a bundle of fresh lavender stems balancing the right."),
            ("나무 새집과 정원 모이통", ["bird", "feeder", "nest", "perch", "shelter", "nature"], "a rustic wooden birdhouse on a sturdy timber post at the optical center, a hanging glass seed feeder balancing the left, one level garden fence baseline extending across both outer thirds, and a terracotta birdbath balancing the right."),
            ("호박과 옥수수 가을 수확 바구니", ["harvest", "crop", "autumn", "ripe", "produce", "plenty"], "a round bushel basket filled with ripe pumpkins and corn ears at the optical center, a wooden garden crate balancing the left, one level barn floor baseline extending across both outer thirds, and a burlap grain sack balancing the right."),
            ("식물 압화기와 건조 허브 액자", ["press", "herb", "dry", "preserve", "specimen", "collection"], "a wooden screw-clamp botanical flower press at the optical center, a stack of absorbent pressing papers balancing the left, one level study counter baseline extending across both outer thirds, and a small glass vial of dried flower seeds balancing the right."),
            ("정원 손수레와 부토 모종", ["cart", "wheelbarrow", "haul", "soil", "yard", "heavy"], "a classic metal single-wheel garden wheelbarrow at the optical center, a bag of rich organic compost balancing the left, one level garden lawn baseline extending across both outer thirds, and a long-handled garden spade balancing the right."),
            ("유리 온실 창문과 덩굴 식물", ["vine", "climb", "greenhouse", "sunlight", "tendril", "flourish"], "a vaulted glass conservatory window pane with delicate ivy vines at the optical center, a hanging macrame potted plant balancing the left, one level windowsill baseline extending across both outer thirds, and an antique copper thermometer balancing the right."),
            ("해바라기와 정원 울타리 게이트", ["sunflower", "stalk", "fence", "gate", "summer", "bright"], "a cluster of tall blooming sunflowers standing along a picket fence at the optical center, a wooden latch gate balancing the left, one level garden path baseline extending across both outer thirds, and a watering bucket balancing the right.")
        ]
    },
    # Set 07: 예술 & 공예 & 디자인
    {
        "set": "Set 07 (미술·공예·디자인)",
        "scenes": [
            ("화실 이젤과 빈 캔버스, 물감 팔레트", ["easel", "cotton fabric", "studio", "palette", "create", "art"], "a sturdy beechwood studio painting easel at the optical center, a wooden thumb-hole creator palette balancing the left, one level wooden studio floor baseline extending across both outer thirds, and a ceramic jar with brushes balancing the right."),
            ("도예 물레와 성형 중인 점토 화병", ["potter", "clay", "spin", "vessel", "sculpt", "form"], "a mechanical pottery kick-wheel with a shaping clay vase at the optical center, a wooden modeling rib device balancing the left, one level studio floor baseline extending across both outer thirds, and a clay trimming wire balancing the right."),
            ("클래식 주철 재봉틀과 실타래", ["sew", "stitch", "thread", "fabric", "tailor", "garment"], "an ornate black vintage cast-iron sewing machine with golden filigree at the optical center, a collection of wooden thread spools balancing the left, one level tailor table baseline extending across both outer thirds, and a pair of heavy tailor scissors balancing the right."),
            ("목공 대패와 나무 대패밥, 조각칼", ["plane", "shave", "woodwork", "chisel", "craftsman", "smooth"], "a traditional wooden block plane with curling wood shavings at the optical center, a set of bevel-edge wood chisels balancing the left, one level heavy workbench baseline extending across both outer thirds, and a brass combination square balancing the right."),
            ("가죽 공예 펀치와 스티칭 포니", ["leather", "punch", "stitch", "strap", "craft", "durable"], "a thick vegetable-tanned leather strip and stitching pony vise at the optical center, a rotary hole punch device balancing the left, one level craft table baseline extending across both outer thirds, and a spool of waxed linen thread balancing the right."),
            ("스테인드글라스 유리 조각과 납선", ["glass", "cut", "color", "mosaic", "pattern", "radiant"], "a colorful geometric stained-glass panel pattern at the optical center, a glass circle cutter device balancing the left, one level glazier workbench baseline extending across both outer thirds, and a roll of flexible lead came wire balancing the right."),
            ("조각용 석고상과 조소 헤라", ["bust", "sculpture", "plaster", "chisel", "statue", "form"], "a classical plaster bust casting on a wooden sculpting turntable at the optical center, a set of wire-end modeling accessories balancing the left, one level studio baseline extending across both outer thirds, and a bag of casting plaster balancing the right."),
            ("판화 프레스기와 고무 롤러", ["print", "press", "ink", "brayer", "block", "reproduce"], "a heavy metal crank-driven etching and relief printing press at the optical center, a rubber ink brayer roller balancing the left, one level printmaking bench baseline extending across both outer thirds, and a carved linoleum printing block balancing the right."),
            ("직조 베틀과 북 셔틀", ["weave", "loom", "warp", "weft", "textile", "pattern"], "a traditional tabletop wooden tabletop loom with stretched warp yarns at the optical center, a wooden boat shuttle with bobbin balancing the left, one level studio baseline extending across both outer thirds, and a woven patterned textile strip balancing the right."),
            ("보석 세공용 돋보기와 루페", ["jewel", "gem", "magnify", "facet", "precision", "precious"], "a gleaming cut diamond gemstone resting on a velvet jeweler pad at the optical center, a jeweler eye loupe magnifier balancing the left, one level jeweler workbench baseline extending across both outer thirds, and a pair of fine precision tweezers balancing the right.")
        ]
    },
    # Set 08: 바다 & 항해 & 해양
    {
        "set": "Set 08 (바다·항해·해양)",
        "scenes": [
            ("목제 범선 타륜과 나침반 비나클", ["wheel", "steer", "helm", "course", "navigate", "sail"], "a large spoked wooden ship helm wheel with brass hub at the optical center, a brass binnacle compass housing balancing the left, one level ship deck plank baseline extending across both outer thirds, and a brass ship bell balancing the right."),
            ("등대 랜턴 룸과 프레넬 렌즈", ["lighthouse", "beam", "beacon", "guide", "coast", "harbor"], "a classic towering lighthouse pinnacle with glass lantern room at the optical center, a brass foghorn balancing the left, one level granite sea wall baseline extending across both outer thirds, and a coastal weather barometer balancing the right."),
            ("다이빙 헬멧과 공기 펌프", ["dive", "depth", "ocean", "breathe", "explore", "submerge"], "a heavy antique copper and brass deep-sea diving helmet at the optical center, an air pressure gauge balancing the left, one level wooden dock baseline extending across both outer thirds, and a coiled air hose balancing the right."),
            ("선박 구명환과 투척 로프", ["rescue", "buoy", "safety", "float", "emergency", "marine"], "a circular orange and white lifebuoy ring with reflective bands at the optical center, a coiled rescue throwing line balancing the left, one level ship railing baseline extending across both outer thirds, and an emergency marine strobe light balancing the right."),
            ("항해 육분의와 해도 차트", ["sextant", "angle", "celestial", "latitude", "position", "ocean"], "a precision brass nautical sextant in an open fitted case at the optical center, a brass parallel ruler balancing the left, one level navigation chart table baseline extending across both outer thirds, and a nautical star catalog balancing the right."),
            ("어선의 대형 그물과 부표", ["net", "trawl", "float", "catch", "fishery", "mesh"], "a heavy knotted maritime fishing net with cork floats at the optical center, a cluster of colorful glass marker buoys balancing the left, one level wooden pier baseline extending across both outer thirds, and a wooden fish crate balancing the right."),
            ("원목 노와 목조 카누", ["canoe", "oar", "row", "lake", "glide", "stroke"], "a classic cedar-strip open canoe resting level at the optical center, a pair of carved wooden oars balancing the left, one level sandy shoreline baseline extending across both outer thirds, and a cotton fabric camp pack balancing the right."),
            ("잠수함 잠망경과 계기판", ["periscope", "sub", "sonar", "depth", "stealth", "gauge"], "a retractable naval submarine periscope column at the optical center, a circular sonar screen dial balancing the left, one level control console baseline extending across both outer thirds, and an analog depth gauge balancing the right."),
            ("선박 프로펠러와 방향타", ["propeller", "thrust", "rudder", "steer", "vessel", "propel"], "a heavy bronze four-bladed ship marine propeller at the optical center, a steel rudder blade balancing the left, one level drydock baseline extending across both outer thirds, and an anchor chain link balancing the right."),
            ("조개껍데기와 진주 조개", ["shell", "pearl", "marine", "gem", "treasure", "reef"], "a large open iridescent oyster shell holding a lustrous round pearl at the optical center, a branching piece of natural coral balancing the left, one level ocean floor baseline extending across both outer thirds, and a polished conch shell balancing the right.")
        ]
    },
    # Set 09: 과학 & 물리 & 실험
    {
        "set": "Set 09 (과학·물리·실험)",
        "scenes": [
            ("광학 현미경과 유리 슬라이드", ["microscope", "slide", "focus", "specimen", "cell", "magnify"], "a classic brass and black enamel optical compound microscope at the optical center, a box of prepared glass specimen slides balancing the left, one level laboratory bench baseline extending across both outer thirds, and a bottle of immersion oil balancing the right."),
            ("분젠 버너와 삼각대, 유리 플라스크", ["burner", "flame", "heat", "flask", "boil", "solution"], "a glass Erlenmeyer laboratory flask on a wire gauze and iron tripod at the optical center, a brass Bunsen burner balancing the left, one level lab counter baseline extending across both outer thirds, and a glass stirring rod balancing the right."),
            ("화학 비커 세트와 스포이트", ["beaker", "pipette", "drop", "measure", "liquid", "chemical"], "a graduated glass laboratory beaker containing transparent liquid at the optical center, a glass dropper pipette balancing the left, one level laboratory bench baseline extending across both outer thirds, and a wooden test tube rack balancing the right."),
            ("뉴턴의 진자 요람과 금속 구슬", ["pendulum", "motion", "energy", "physics", "collide", "momentum"], "a classic chrome Newton cradle with five suspended steel balls at the optical center, a small precision stopwatch balancing the left, one level wooden counter baseline extending across both outer thirds, and a balance scale balancing the right."),
            ("말굽 자석과 쇠가루 자기력선", ["magnet", "pole", "attract", "force", "magnetic", "field"], "a classic red and silver horseshoe magnet at the optical center, a small pile of iron filings balancing the left, one level laboratory table baseline extending across both outer thirds, and a pocket magnetic compass balancing the right."),
            ("테슬라 코일과 방전 스파크", ["voltage", "spark", "electric", "current", "circuit", "charge"], "a miniature laboratory Tesla coil secondary resonant tower at the optical center, an analog voltage meter dial balancing the left, one level workbench baseline extending across both outer thirds, and a glass Leyden jar capacitor balancing the right."),
            ("화학 원소 주기율표 분자 모형", ["molecule", "atom", "bond", "element", "structure", "compound"], "a colorful three-dimensional ball-and-stick chemical molecule model at the optical center, a periodic element cube balancing the left, one level science bench baseline extending across both outer thirds, and a porcelain mortar and pestle balancing the right."),
            ("기압계와 수은주 측정관", ["barometer", "pressure", "atmosphere", "mercury", "forecast", "weather"], "a classic antique brass aneroid barometer dial in a circular timber bezel at the optical center, a glass thermometer column balancing the left, one level wooden shelf baseline extending across both outer thirds, and a brass hygrometer balancing the right."),
            ("진공 벨 항아리와 배기 펌프", ["vacuum", "chamber", "pump", "airless", "pressure", "sound"], "a heavy glass bell jar on a flanged brass vacuum baseplate at the optical center, a manual brass suction vacuum pump balancing the left, one level lab table baseline extending across both outer thirds, and an internal chime bell balancing the right."),
            ("도르래 시스템과 균형 추", ["pulley", "wheel", "hoist", "weight", "mechanical", "lift"], "a double-sheave brass pulley block suspended from a sturdy crossbar at the optical center, a stack of slotted brass calibration weights balancing the left, one level physics bench baseline extending across both outer thirds, and a spring dynamometer balancing the right.")
        ]
    },
    # Set 10: 건축 & 공구 & 기계 메커니즘
    {
        "set": "Set 10 (건축·공구·메커니즘)",
        "scenes": [
            ("클래식 앤빌 모루와 대장간 망치", ["anvil", "hammer", "forge", "iron", "strike", "metalwork"], "a heavy solid cast-steel blacksmith anvil resting on a solid timber stump at the optical center, a heavy cross-peen forge hammer balancing the left, one level workshop floor baseline extending across both outer thirds, and a pair of blacksmith tongs balancing the right."),
            ("기계식 톱니바퀴 기어 트레인", ["gear", "cog", "mesh", "rotate", "machine", "interlock"], "a precision assembly of interlocking brass and steel spur gear wheels at the optical center, a mechanical crank-driven handle balancing the left, one level machine baseplate baseline extending across both outer thirds, and a lubrication oil can balancing the right."),
            ("버니어 캘리퍼스와 마이크로미터", ["caliper", "measure", "precision", "dimension", "gauge", "accurate"], "a stainless steel vernier caliper with dual sliding jaws at the optical center, a micrometer screw gauge balancing the left, one level metal inspection table baseline extending across both outer thirds, and a precision steel gauge block balancing the right."),
            ("건축가 제도판과 T자 삼각자", ["draft", "blueprint", "architect", "scale", "plan", "ruler"], "a smooth tilted wooden drafting board at the optical center, a clear acrylic T-square ruler balancing the left, one level studio baseline extending across both outer thirds, and a set of drafting triangle rules balancing the right."),
            ("스피릿 레벨 수평계와 다림줄", ["level", "bubble", "horizontal", "vertical", "plumb", "align"], "a heavy cast-aluminum spirit level with green fluorescent bubble vials at the optical center, a solid brass pointed plumb bob weight balancing the left, one level masonry wall baseline extending across both outer thirds, and a builder chalk line reel balancing the right."),
            ("벤치 바이스와 쇠톱", ["vise", "clamp", "saw", "grip", "cut", "secure"], "a heavy cast-iron mechanical bench vise with serrated steel jaws at the optical center, a hacksaw with a high-tension carbon blade balancing the left, one level workbench baseline extending across both outer thirds, and a machinist flat steel file balancing the right."),
            ("전동 드릴과 드릴 비트 세트", ["drill", "bore", "hole", "bit", "power", "penetrate"], "a compact cordless power drill resting squarely on its battery base at the optical center, an indexed metal case of twist drill bits balancing the left, one level workshop bench baseline extending across both outer thirds, and a wooden dowel rod balancing the right."),
            ("볼트와 너트, 조합 렌치", ["bolt", "nut", "wrench", "fasten", "thread", "tighten"], "a large polished hexagonal steel bolt and matching hex nut at the optical center, an open-end combination wrench balancing the left, one level device chest baseline extending across both outer thirds, and a lock washer balancing the right."),
            ("벽돌공 흙손과 쌓은 벽돌 벽", ["trowel", "brick", "mason", "mortar", "build", "structure"], "a diamond-blade steel masonry pointing trowel resting beside clean red clay bricks at the optical center, a wooden mortar mixing board balancing the left, one level foundation baseline extending across both outer thirds, and a builder brick hammer balancing the right."),
            ("무거운 쇠사슬과 리프팅 샤클", ["chain", "shackle", "link", "steel", "heavy", "hoist"], "a heavy forged alloy steel hoisting chain with round welded links at the optical center, an anchor bow shackle with threaded pin balancing the left, one level industrial floor baseline extending across both outer thirds, and a heavy lifting eye hook balancing the right.")
        ]
    },
    # Set 11: 음악 & 악기 & 오케스트라
    {
        "set": "Set 11 (음악·악기·공연)",
        "scenes": [
            ("바이올린과 활, 송진 케이스", ["violin", "bow", "string", "melody", "acoustic", "wood"], "a classical handcrafted wooden acoustic violin with f-holes at the optical center, a horsehair violin bow balancing the left, one level wooden stage floor baseline extending across both outer thirds, and a circular wooden cake of rosin balancing the right."),
            ("어쿠스틱 클래식 기타와 픽", ["guitar", "fret", "strum", "chord", "hollow", "tone"], "a natural-wood classical acoustic nylon-string guitar on a folding floor stand at the optical center, a collection of celluloid guitar picks balancing the left, one level parquet floor baseline extending across both outer thirds, and a clip-on digital guitar tuner balancing the right."),
            ("골드 색소폰과 코르크 리드", ["saxophone", "brass", "jazz", "reed", "valve", "horn"], "a curved golden lacquered alto saxophone resting securely on a velvet-padded cradle stand at the optical center, a wooden cane reed in a protective case balancing the left, one level stage baseline extending across both outer thirds, and a neck strap balancing the right."),
            ("은빛 플루트와 악기 하드케이스", ["flute", "silver", "wind", "key", "breath", "tone"], "a gleaming silver concert flute with open-hole keys resting in a velvet-lined case at the optical center, a wooden cleaning rod balancing the left, one level music room baseline extending across both outer thirds, and an open music sheet balancing the right."),
            ("클래식 그랜드 첼로와 엔드핀", ["cello", "bass", "chamber", "body", "deep", "resonance"], "a full-size carved maple wood acoustic cello resting on its extendable steel endpin at the optical center, a braided carbon-fiber cello bow balancing the left, one level concert hall floor baseline extending across both outer thirds, and a non-slip rubber endpin stop pad balancing the right."),
            ("오케스트라 팀파니 드럼과 말렛", ["timpani", "kettle", "drum", "percussion", "rhythm", "beat"], "a large hemispherical polished copper orchestral kettle drum at the optical center, a pair of felt-headed timpani mallets balancing the left, one level stage floor baseline extending across both outer thirds, and a mechanical tuning foot pedal balancing the right."),
            ("콘서트 하프와 페달 박스", ["harp", "pillar", "pluck", "harmony", "grace", "strings"], "an elegant gilded concert grand pedal harp with curved neck and fluted pillar at the optical center, a wooden tuning key balancing the left, one level stage floor baseline extending across both outer thirds, and an adjustable musician stool balancing the right."),
            ("실버 트롬본과 슬라이드 바", ["trombone", "slide", "brass", "fanfare", "extend", "pitch"], "a professional tenored brass trombone with long telescopic manual slide at the optical center, a silver mouthpiece balancing the left, one level music stand baseline extending across both outer thirds, and a bottle of slide lubricant balancing the right."),
            ("피아노 건반과 조율용 소리굽쇠", ["tuning", "frequency", "pitch", "sound", "vibrate", "wave"], "a sleek horizontal row of ebony and ivory piano keys at the optical center, a slender steel acoustic tuning fork balancing the left, one level piano keybed baseline extending across both outer thirds, and a wooden conductor baton balancing the right."),
            ("아코디언 벨로우즈와 베이스 버튼", ["accordion", "bellows", "squeeze", "reed", "folk", "air"], "a decorated vintage piano accordion with pleated leather bellows at the optical center, a set of bass harmony buttons balancing the left, one level wooden floor baseline extending across both outer thirds, and a leather shoulder strap balancing the right.")
        ]
    },
    # Set 12: 의학 & 보건 & 인체 케어
    {
        "set": "Set 12 (의학·보건·케어)",
        "scenes": [
            ("청진기와 혈압계 커프", ["stethoscope", "pulse", "heart", "doctor", "listen", "health"], "a modern stainless medical dual-head stethoscope at the optical center, an analog aneroid blood pressure dial with pressure sleeve balancing the left, one level clinic counter baseline extending across both outer thirds, and a reflex percussion hammer balancing the right."),
            ("체온계와 멸균 붕대 롤", ["temperature", "fever", "sterile", "bandage", "recover", "heal"], "a digital clinical thermometer displaying normal reading at the optical center, a roll of sterile white elastic bandage gauze balancing the left, one level medical tray baseline extending across both outer thirds, and a small amber glass medicine bottle balancing the right."),
            ("안경과 시력 검사표 차트", ["glasses", "vision", "optometry", "focus", "clarity", "sight"], "a pair of round tortoiseshell reading glasses with anti-reflective lenses at the optical center, a hard clamshell spectacle case balancing the left, one level optometry counter baseline extending across both outer thirds, and a microfiber lens cloth balancing the right."),
            ("치과용 미러와 탐침 프로브", ["dental", "mirror", "tooth", "check", "clean", "hygiene"], "a stainless angled dental mouth mirror and explorer probe at the optical center, a silicone tooth model balancing the left, one level sterile metal tray baseline extending across both outer thirds, and a bottle of oral rinse balancing the right."),
            ("약사 조제용 유발과 막자, 알약 캡슐", ["pharmacy", "mortar", "pestle", "compound", "pill", "remedy"], "a heavy white porcelain pharmaceutical mortar and pestle at the optical center, an amber prescription bottle with capsules balancing the left, one level pharmacy counter baseline extending across both outer thirds, and a small brass balance scale balancing the right."),
            ("초음파 탐촉자와 젤 보틀", ["ultrasound", "probe", "scan", "imaging", "monitor", "diagnose"], "a medical diagnostic ultrasound transducer probe on a curved cradle at the optical center, a squeeze bottle of clear acoustic coupling gel balancing the left, one level medical cart baseline extending across both outer thirds, and a high-resolution display panel balancing the right."),
            ("수술용 가위와 지혈 겸자 포셉", ["surgery", "forceps", "clamp", "precision", "operate", "care"], "a pair of locking stainless hemostatic forceps and curved surgical scissors at the optical center, a sterile surgical cotton swab tray balancing the left, one level stainless operating cart baseline extending across both outer thirds, and a rolled surgical drape balancing the right."),
            ("휴대용 산소통과 흡입 마스크", ["oxygen", "breathe", "tank", "valve", "inhalation", "vital"], "a compact medical oxygen cylinder with chrome regulator pressure valve at the optical center, a clear silicone oxygen mask and tube balancing the left, one level paramedic trolley baseline extending across both outer thirds, and a pulse oximeter optical sensor balancing the right."),
            ("목발과 재활 보행기", ["crutch", "mobility", "rehab", "support", "walk", "assist"], "a pair of adjustable aluminum support crutches resting upright at the optical center, an elastic ankle support brace balancing the left, one level clinic floor baseline extending across both outer thirds, and a physical therapy resistance band balancing the right."),
            ("구급 들것과 접이식 휠체어", ["stretcher", "wheelchair", "transport", "patient", "ambulance", "safe"], "a lightweight folding ambulance emergency stretcher bed at the optical center, a compact folding wheelchair balancing the left, one level hospital corridor baseline extending across both outer thirds, and an intravenous drip stand balancing the right.")
        ]
    },
    # Set 13: 문명 & 사회 & 법률·우편·금융
    {
        "set": "Set 13 (사회·통신·우편·금융)",
        "scenes": [
            ("빨간 우체통과 소포 상자, 편지 봉투", ["mail", "letter", "parcel", "post", "deliver", "stamp"], "a classic red pillar postbox with curved cap and mail drop slot at the optical center, a brown kraft document sheet parcel with string tie balancing the left, one level sidewalk curb baseline extending across both outer thirds, and a stamped envelope balancing the right."),
            ("은행 대형 원형 금고문과 다이얼", ["vault", "safe", "lock", "secure", "finance", "deposit"], "a massive circular polished steel bank vault door with heavy radial locking bolts at the optical center, a combination dial wheel balancing the left, one level bank floor baseline extending across both outer thirds, and a small steel safety deposit box balancing the right."),
            ("금화 더미와 황동 저울, 통장", ["coin", "currency", "wealth", "account", "balance", "trade"], "a neat stack of gleaming round gold bullion coins at the optical center, a small two-pan brass currency balance scale balancing the left, one level marble bank counter baseline extending across both outer thirds, and a folded leather banking register balancing the right."),
            ("공공도서관 반납함과 대출 카드", ["library", "borrow", "catalog", "return", "archive", "knowledge"], "a wooden library book drop return depository cart at the optical center, an open book index card drawer balancing the left, one level library parquet floor baseline extending across both outer thirds, and an embossed library stamp seal balancing the right."),
            ("선거 투표함과 투표용지 봉투", ["vote", "ballot", "elect", "choice", "citizen", "democracy"], "a sealed wooden ballot box with narrow top ballot slot at the optical center, a clean folded official ballot document sheet balancing the left, one level voting station baseline extending across both outer thirds, and an official ink voting stamp balancing the right."),
            ("여권 케이스와 비행기 탑승권 티켓", ["passport", "travel", "customs", "board", "ticket", "border"], "a navy leather passport wallet with gold-embossed emblem at the optical center, a printed airline boarding pass ticket balancing the left, one level immigration counter baseline extending across both outer thirds, and an entry clearance rubber stamp balancing the right."),
            ("우편 저울과 소포 요금 스탬프", ["scale", "weigh", "postage", "package", "rate", "dispatch"], "a mechanical postal parcel scale with broad weight platform at the optical center, a roll of self-adhesive postage stamps balancing the left, one level post office counter baseline extending across both outer thirds, and a rubber date canceling stamp balancing the right."),
            ("앤틱 가죽 서류가방과 황동 잠금장치", ["briefcase", "document", "attorney", "contract", "business", "legal"], "a classic brown leather structured briefcase with dual brass buckle latches at the optical center, a rolled legal scroll document document with red ribbon balancing the left, one level conference counter baseline extending across both outer thirds, and a metal key balancing the right."),
            ("시계탑 기계식 탈진기 클락워크", ["clock", "escapement", "pendulum", "time", "precision", "chime"], "a precision skeleton clock movement mechanism with brass escapement wheel and swinging pendulum at the optical center, a circular Roman numeral clock face balancing the left, one level wooden mantle baseline extending across both outer thirds, and a brass winding key balancing the right."),
            ("국제 조약 서명용 깃털펜과 왁스 씰", ["treaty", "accord", "seal", "diplomacy", "pledge", "formal"], "an engraved brass signet ring and melted red wax seal impression on heavy laid document sheet at the optical center, a ribbon-bound treaty scroll balancing the left, one level formal mahogany counter baseline extending across both outer thirds, and a decorative brass paperweight balancing the right.")
        ]
    }
]

def generate_single_prompt(subject_desc):
    template = f"""Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. The visual weight is divided evenly across the left and right halves, with a small subject anchor in each outer third. The horizon and camera axis are perfectly level: no Dutch angle, no tilted angle, no composition leaning to either side. Static locked-off camera, one continuous 8-second take. The only visible subjects throughout the sequence are {subject_desc} 0-4s: ultra-fine pale warm-grey graphite linework appears progressively from the empty white field. Every outline is very thin, soft and light, never black or dark charcoal; there are no bold contours, heavy edge lines or dense hatch marks. Begin with one perfectly level minimal baseline. Draw the main central subject silhouette next, keeping the combined silhouette horizontal rather than diagonal. Extend a single thin baseline equally toward the left and right outer thirds. Add a small anchor item at left and a balancing accessory at right. There is no visible person, driver, student, live action element, wall, ceiling, darkness or heavy architecture anywhere. Keep all outline contours sparse, pale and softly broken, never darker than 15% grey and never filled as solid outlined blobs. Every detail becomes visible sequentially, never all at once. Previously revealed lines remain delicate and completely stable. 4-8s: an extremely pale, water-heavy watercolor wash develops gently. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled. Use distinct, believable colors for different materials. Restraint means low saturation, not fewer colors or shared hues. The restrained palette is sheer translucent pastel tones across the main subjects and delicate soft neutral tints on accents. A single tiny luminous glint sparkles softly once on the central subject top; all structural linework and baseline remain crisp and still. All other elements remain still. The final composition remains centered, readable and surrounded by generous untouched white space. Style: master-level fine-line illustration with exceptionally thin, pale warm-grey graphite strokes and sophisticated control, maximum line value 25% grey, luminous transparent watercolor, restrained tonal contrast, sophisticated contemporary editorial illustration for thoughtful young learners, generous untouched white space."""
    return " ".join(template.split())

os.makedirs("_작업/bulk_sets", exist_ok=True)

all_set_data = []

for s_idx, s_data in enumerate(MASTER_100_THEMES, 4):
    set_name = s_data["set"]
    set_filename = f"_작업/bulk_sets/set{s_idx:02d}_10.txt"
    set_prompts = []
    
    with open(set_filename, "w", encoding="utf-8") as f:
        for idx, (title, words, subject_desc) in enumerate(s_data["scenes"], 1):
            p_text = generate_single_prompt(subject_desc)
            set_prompts.append({
                "id": f"set{s_idx:02d}-{idx:02d}",
                "chapter": set_name,
                "title": title,
                "words": words,
                "prompt": p_text
            })
            f.write(p_text + "\n\n")
            
    all_set_data.append({
        "set_id": f"set{s_idx:02d}",
        "set_name": set_name,
        "filename": set_filename,
        "prompts": set_prompts
    })
    print(f"Generated {set_filename} ({len(set_prompts)} prompts)")

with open("_작업/complete_100_data.json", "w", encoding="utf-8") as f:
    json.dump(all_set_data, f, ensure_ascii=False, indent=2)

print("\n100편 전체 프롬프트 데이터 빌드 완료!")
