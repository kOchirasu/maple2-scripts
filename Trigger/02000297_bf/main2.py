""" trigger/02000297_bf/main2.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1001,1002,1003,1004], auto_target=False)
        self.destroy_monster(spawn_ids=[1005])
        self.destroy_monster(spawn_ids=[1006])
        self.destroy_monster(spawn_ids=[1007])
        self.set_mesh(trigger_ids=[107]) # InvisibleBarrier
        self.set_mesh(trigger_ids=[31000,31001,31002,31003,31004,31005], visible=True) # Stairs
        self.set_portal(portal_id=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return LoadingDelay(self.ctx)


class LoadingDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[107], visible=True) # InvisibleBarrier
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=888888)
        self.move_npc(spawn_id=1004, patrol_name='MS2PatrolData1')
        self.set_skip(state=연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 레논01(self.ctx)


class 레논01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000064, script='$02000297_BF__MAIN2__0$', time=2)
        self.set_skip(state=연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 벨라01(self.ctx)


class 벨라01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000057, script='$02000297_BF__MAIN2__1$', time=3)
        self.set_dialogue(type=2, spawn_id=11000057, script='$02000297_BF__MAIN2__2$', time=3)
        self.set_skip(state=연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9925):
            return 벨라02(self.ctx)


class 벨라02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1002, patrol_name='MS2PatrolData3')
        self.set_skip(state=연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 레논02(self.ctx)


class 레논02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000064, script='$02000297_BF__MAIN2__3$', time=2)
        self.set_skip(state=연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 레논03(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=4)


class 레논03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1004])
        self.destroy_monster(spawn_ids=[1001])
        self.spawn_monster(spawn_ids=[1005], auto_target=False)
        self.spawn_monster(spawn_ids=[1008], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 블랙01(self.ctx)


class 블랙01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_npc(spawn_id=1003, patrol_name='MS2PatrolData0')
        self.set_dialogue(type=2, spawn_id=11000006, script='$02000297_BF__MAIN2__4$', time=2)
        self.set_dialogue(type=2, spawn_id=11000006, script='$02000297_BF__MAIN2__5$', time=2)
        self.set_dialogue(type=2, spawn_id=11000057, script='$02000297_BF__MAIN2__6$', time=3)
        self.set_skip(state=연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 카메라복귀(self.ctx)


class 카메라복귀(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1002])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=888888, enable=False)
        self.set_mesh(trigger_ids=[107]) # InvisibleBarrier
        self.set_mesh(trigger_ids=[31000,31001,31002,31003,31004,31005]) # Stairs
        self.spawn_monster(spawn_ids=[6200], auto_target=False)
        self.destroy_monster(spawn_ids=[1003])
        self.destroy_monster(spawn_ids=[1002])
        self.destroy_monster(spawn_ids=[1001])
        self.destroy_monster(spawn_ids=[1004])
        self.spawn_monster(spawn_ids=[1005], auto_target=False)
        self.spawn_monster(spawn_ids=[1006])
        self.spawn_monster(spawn_ids=[1008], auto_target=False)
        self.set_user_value(trigger_id=999991, key='BattleStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[6200]):
            return 엔딩연출1(self.ctx)


class 엔딩연출1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[31000,31001,31002,31003,31004,31005], visible=True) # Stairs

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 엔딩연출(self.ctx)


class 엔딩연출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=888888)
        self.destroy_monster(spawn_ids=[1006])
        self.spawn_monster(spawn_ids=[1007], auto_target=False)
        self.move_npc(spawn_id=1007, patrol_name='MS2PatrolData5')
        self.set_skip(state=연출종료2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 블랙03(self.ctx)


class 블랙03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000006, script='$02000297_BF__MAIN2__7$', time=3)
        self.set_dialogue(type=2, spawn_id=11000064, script='$02000297_BF__MAIN2__8$', time=3)
        self.set_dialogue(type=2, spawn_id=11000006, script='$02000297_BF__MAIN2__9$', time=3)
        self.set_skip(state=연출종료2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=11101):
            return 연출종료2(self.ctx)


class 연출종료2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_skip() # Missing State: State
        self.select_camera(trigger_id=888888, enable=False)
        self.destroy_monster(spawn_ids=[1005])
        self.destroy_monster(spawn_ids=[1008])
        self.destroy_monster(spawn_ids=[1007])
        self.set_achievement(trigger_id=9001, type='trigger', achieve='ClearKatramusSecond')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear()
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)


initial_state = 대기
