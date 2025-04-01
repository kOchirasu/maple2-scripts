""" trigger/02000410_bf/event01.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=750) >= 1:
            # MS2TriggerBox   TriggerObjectID = 750, 이 트리거 박스 안에 플레이어가 한명이라도 체크 되면,   750은 스타팅 지점 전투판 다  포함되는 범위, 700은 전투판만 포함되는 범위
            return 전투시작잠시대기(self.ctx)


class 전투시작잠시대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 전투시작_인페르녹전함(self.ctx)


class 전투시작_인페르녹전함(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # ##  01. 일러스트 대화창 연출 넣기  ##
        self.show_guide_summary(entity_id=20041002, text_id=20041002)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 첫번째페이즈_인페르녹전함(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=20041002)


class 첫번째페이즈_인페르녹전함(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='AirshipBalrogCrimsonBroken') == 1:
            # 1페이즈 인페르녹의 전함이 파괴될때   AirshipBalrogCrimsonBroken = 1 신호를 받을때까지 여기서 대기
            return 인페르녹전함파괴연출(self.ctx)


class 인페르녹전함파괴연출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # ##  02. 일러스트 대화창 연출 넣기  ##
        self.show_guide_summary(entity_id=20041003, text_id=20041003)
        self.side_npc_talk(npc_id=11003536, illust='Neirin_normal', duration=5000, script='$02000410_BF__Event01__0$', voice='ko/Npc/00002167')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 인페르녹전함파괴연출2(self.ctx)


class 인페르녹전함파괴연출2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # ##  02. 일러스트 대화창 연출 넣기  ##
        self.side_npc_talk(npc_id=11003533, illust='Bliche_nomal', duration=5000, script='$02000410_BF__Event01__1$', voice='ko/Npc/00002158')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 두번째페이즈_인페르녹전함(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=20041003)


class 두번째페이즈_인페르녹전함(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='AirshipBalrogCrimsonFlameBroken') == 1:
            # 2페이즈 인페르녹의 전함이 파괴될때   AirshipBalrogCrimsonFlameBroken = 1 신호를 받을때까지 여기서 대기
            return 인페르녹전함파괴_인페르녹등장연출(self.ctx)


class 인페르녹전함파괴_인페르녹등장연출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # ##  03. 일러스트 대화창 연출 넣기  ##
        self.show_guide_summary(entity_id=20041004, text_id=20041004)
        self.side_npc_talk(npc_id=11003536, illust='Neirin_normal', duration=5000, script='$02000410_BF__Event01__2$', voice='ko/Npc/00002168')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 인페르녹전함파괴_인페르녹등장연출2(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=20041004)


class 인페르녹전함파괴_인페르녹등장연출2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # ##  03. 일러스트 대화창 연출 넣기  ##
        self.side_npc_talk(npc_id=11003536, illust='Neirin_surprise', duration=3000, script='$02000410_BF__Event01__3$', voice='ko/Npc/00002169')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 인페르녹전함파괴_인페르녹등장연출3(self.ctx)


class 인페르녹전함파괴_인페르녹등장연출3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # ##  03. 일러스트 대화창 연출 넣기  ##
        self.side_npc_talk(npc_id=11003533, illust='Bliche_closeEye', duration=4000, script='$02000410_BF__Event01__4$', voice='ko/Npc/00002159')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 인페르녹전함파괴_인페르녹등장연출4(self.ctx)


class 인페르녹전함파괴_인페르녹등장연출4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # ##  03. 일러스트 대화창 연출 넣기  ##
        self.side_npc_talk(npc_id=11003536, illust='Neirin_surprise', duration=5000, script='$02000410_BF__Event01__5$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 인페르녹전함파괴_인페르녹등장연출5(self.ctx)


class 인페르녹전함파괴_인페르녹등장연출5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # ##  03. 일러스트 대화창 연출 넣기  ##
        self.side_npc_talk(npc_id=11003536, illust='Neirin_surprise', duration=5000, script='$02000410_BF__Event01__6$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 인페르녹전함파괴_인페르녹등장연출6(self.ctx)


class 인페르녹전함파괴_인페르녹등장연출6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # ##  03. 일러스트 대화창 연출 넣기  ##
        self.side_npc_talk(npc_id=11003533, illust='Bliche_nomal', duration=5000, script='$02000410_BF__Event01__7$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 세번째페이즈_인페르녹등장(self.ctx)


class 세번째페이즈_인페르녹등장(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BalrogMagicBursterBattlePhase') == 1: # 15분 다 지나 끝난 이후  실패한 경우
            # 인페르녹과 전투 시작할 때 몬스터 AI에서 이 신호를 보낼때까지 대기
            # 즉  BalrogMagicBursterBattlePhase = 1 신호를 AI에서 부터 트리거가  받을때까지 여기서 대기
            return None # Missing State: 성공이벤트실행
        if self.user_value(key='BalrogMagicBursterBattlePhase') == 1:
            # 인페르녹과 전투 시작할 때 몬스터 AI에서 이 신호를 보낼때까지 대기
            # 즉  BalrogMagicBursterBattlePhase = 1 신호를 AI에서 부터 트리거가  받을때까지 여기서 대기
            return None # Missing State: 실패이벤트실행


initial_state = Ready
