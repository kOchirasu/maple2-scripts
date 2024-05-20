""" trigger/02010055_bf/scene02.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 룸체크(self.ctx)


class 룸체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.is_dungeon_room():
            return 난이도체크(self.ctx)
        if not self.is_dungeon_room():
            return 퀘스트던전대기(self.ctx)


class 난이도체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_level() == 2:
            return 레이드대기(self.ctx)
        if self.dungeon_level() == 3:
            return None # Missing State: 카오스레이드


class 퀘스트던전대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2299]):
            return 영상준비(self.ctx)


class 레이드대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2099]):
            return 영상준비(self.ctx)


class 카오스레이드대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2199]):
            return 영상준비(self.ctx)


class 연출시작딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=302)
        self.spawn_monster(spawn_ids=[1002,1003,1004], auto_target=False)
        self.set_skip(state=NPC이동)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 스타츠대사01(self.ctx)


class 스타츠대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip(state=NPC이동)
        self.set_dialogue(type=2, spawn_id=11001292, script='$02010055_BF__SCENE02__0$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 타라대사01(self.ctx)


class 타라대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip(state=NPC이동)
        self.set_dialogue(type=2, spawn_id=11001218, script='$02010055_BF__SCENE02__1$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 스타츠대사02(self.ctx)


class 스타츠대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip(state=NPC이동)
        self.set_dialogue(type=2, spawn_id=11001292, script='$02010055_BF__SCENE02__2$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return NPC이동(self.ctx)


class NPC이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=302, enable=False)
        self.move_npc(spawn_id=1002, patrol_name='MS2PatrolData_A')
        self.move_npc(spawn_id=1003, patrol_name='MS2PatrolData_A')
        self.move_npc(spawn_id=1004, patrol_name='MS2PatrolData_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            self.destroy_monster(spawn_ids=[1002,1003,1004])
            return 종료(self.ctx)


class 영상준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_timer(timer_id='21', seconds=10)
        self.select_camera_path(path_ids=[601,602], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='21'):
            return 영상재생(self.ctx)


class 영상재생(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(file_name='common\\KarKarBossEvent.usm', movie_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=10000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작대기중
