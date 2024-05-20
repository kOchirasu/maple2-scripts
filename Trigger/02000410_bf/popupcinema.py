""" trigger/02000410_bf/popupcinema.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=750) >= 1:
            # MS2TriggerBox   TriggerObjectID = 750, 이 트리거 박스 안에 플레이어가 한명이라도 체크 되면      750은 스타팅 지점 전투판 다  포함되는 범위, 700은 전투판만 포함되는 범위
            return 시작연출준비(self.ctx)


class 시작연출준비(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return 전투시작01(self.ctx)


class 전투시작01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11003533, illust='Bliche_nomal', duration=5000, script='$02000410_BF__PopUpCinema__0$', voice='ko/Npc/00002157')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 전투시작02(self.ctx)


class 전투시작02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # duration="0" 은 영상 끝날때까지 계속 출력
        self.side_npc_movie(usm='Common/WorldInvasionScene1.usm', duration=0)
        self.side_npc_talk(npc_id=11003536, illust='Neirin_normal', duration=5000, script='$02000410_BF__PopUpCinema__1$', voice='ko/Npc/00002166')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 전투시작03(self.ctx)


class 전투시작03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11003795, illust='infernog_nomal', duration=5000, script='$02000410_BF__PopUpCinema__2$', voice='ko/Monster/60000724')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 전투시작04(self.ctx)


class 전투시작04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11003795, illust='infernog_nomal', duration=5000, script='$02000410_BF__PopUpCinema__3$', voice='ko/Monster/60000725')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 전투시작05(self.ctx)


class 전투시작05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11000144, illust='tristan_normal', duration=5000, script='$02000410_BF__PopUpCinema__4$', voice='ko/Npc/00002172')

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_play_time() >= 240:
            # 던전 플레이 시간 체크하는 이 로직은 맵으로 바로 들어가지 말고, 던전로직을 통해서 정식으로 입장해야 작동함
            return 두번째팝업영상출력(self.ctx)


class 두번째팝업영상출력(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 두번째 영상출력하기
        # duration="0" 은 영상 끝날때까지 계속 출력
        self.side_npc_movie(usm='Common/WorldInvasionScene2.usm', duration=0)
        self.side_npc_talk(npc_id=11003536, illust='Neirin_normal', duration=5000, script='$02000410_BF__PopUpCinema__5$', voice='ko/Npc/00002178')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 두번째팝업영상출력02(self.ctx)


class 두번째팝업영상출력02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 두번째 영상출력하기
        self.side_npc_talk(npc_id=11003533, illust='Bliche_nomal', duration=5000, script='$02000410_BF__PopUpCinema__6$', voice='ko/Npc/00002173')

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_play_time() >= 480:
            # 던전 플레이 시간 체크하는 이 로직은 맵으로 바로 들어가지 말고, 던전로직을 통해서 정식으로 입장해야 작동함
            return 세번째팝업영상출력(self.ctx)


class 세번째팝업영상출력(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 두번째 영상출력하기
        self.side_npc_talk(npc_id=11003536, illust='Neirin_normal', duration=5000, script='$02000410_BF__PopUpCinema__7$', voice='ko/Npc/00002179')
        # duration="0" 은 영상 끝날때까지 계속 출력
        self.side_npc_movie(usm='Common/WorldInvasionScene3.usm', duration=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 세번째팝업영상출력02(self.ctx)


class 세번째팝업영상출력02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 두번째 영상출력하기
        self.side_npc_talk(npc_id=11003536, illust='Bliche_nomal', duration=5000, script='$02000410_BF__PopUpCinema__8$', voice='ko/Npc/00002174')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 세번째팝업영상출력03(self.ctx)


class 세번째팝업영상출력03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 두번째 영상출력하기
        self.side_npc_talk(npc_id=11003536, illust='Neirin_normal', duration=5000, script='$02000410_BF__PopUpCinema__9$', voice='ko/Npc/00002180')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 세번째팝업영상출력04(self.ctx)


class 세번째팝업영상출력04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 두번째 영상출력하기
        self.side_npc_talk(npc_id=11003533, illust='Bliche_nomal', duration=5000, script='$02000410_BF__PopUpCinema__10$', voice='ko/Npc/00002175')

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_play_time() >= 720:
            # 던전 플레이 시간 체크하는 이 로직은 맵으로 바로 들어가지 말고, 던전로직을 통해서 정식으로 입장해야 작동함
            return 네번째팝업영상출력(self.ctx)


class 네번째팝업영상출력(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 네번째팝업영상출력
        # duration="0" 은 영상 끝날때까지 계속 출력
        self.side_npc_movie(usm='Common/WorldInvasionScene4.usm', duration=0)
        self.side_npc_talk(npc_id=11003536, illust='Neirin_normal', duration=5000, script='$02000410_BF__PopUpCinema__11$', voice='ko/Npc/00002181')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 네번째팝업영상출력02(self.ctx)


class 네번째팝업영상출력02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 네번째팝업영상출력
        self.side_npc_talk(npc_id=11003533, illust='Bliche_nomal', duration=5000, script='$02000410_BF__PopUpCinema__12$', voice='ko/Npc/00002176')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 트리거종료(self.ctx)


# 팝업영상 다 띄우고 종료하기
class 트리거종료(trigger_api.Trigger):
    pass


initial_state = Ready
