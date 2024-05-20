""" trigger/52010009_qd/main.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000866], state=0) # 컨테이너를 반응 가능한 상태로 변경
        self.set_interact_object(trigger_ids=[10000880], state=0) # 컨테이너를 반응 가능한 상태로 변경
        self.set_interact_object(trigger_ids=[10000915], state=0) # 컨테이너를 반응 가능한 상태로 변경

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[20002091], quest_states=[1]):
            return Event_01_Idle(self.ctx)


class Event_01_Idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return Event_01(self.ctx)


class Event_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=110, text_id=40010) # 적을 모두 처치하세요
        self.spawn_monster(spawn_ids=[101], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101]):
            # 맵 내 몬스터 한 무리를 죽이면
            return Event_02(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=110)
        self.set_interact_object(trigger_ids=[10000866], state=1) # 컨테이너를 반응 가능한 상태로 변경


class Event_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=111, text_id=25201901) # 수리공이 숨어있는 컨테이너를 찾으세요.

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000866], state=0):
            # 컨테이너를 반응 시키면
            return Event_03(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=111)
        self.spawn_monster(spawn_ids=[111], auto_target=False) # 그 안에 숨어있던 수리공 NPC들이 리젠
        self.set_dialogue(type=1, spawn_id=111, script='$52010009_QD__MAIN__0$', time=3, arg5=1)
        self.move_npc(spawn_id=111, patrol_name='MS2PatrolData0_1001')


class Event_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=110, text_id=40010) # 적을 모두 처치하세요
        self.spawn_monster(spawn_ids=[102], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[102]):
            # 맵 내 몬스터 한 무리를 죽이면
            return Event_04(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=110)
        self.set_interact_object(trigger_ids=[10000880], state=1) # 컨테이너를 반응 가능한 상태로 변경


class Event_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=111, text_id=25201901) # 수리공이 숨어있는 컨테이너를 찾으세요.

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000880], state=0):
            # 컨테이너를 반응 시키면
            return Event_05(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=111)
        self.spawn_monster(spawn_ids=[112], auto_target=False) # 그 안에 숨어있던 수리공 NPC들이 리젠
        self.set_dialogue(type=1, spawn_id=112, script='$52010009_QD__MAIN__1$', time=3, arg5=1)
        self.move_npc(spawn_id=112, patrol_name='MS2PatrolData0_1001')


class Event_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=110, text_id=40010) # 적을 모두 처치하세요
        self.spawn_monster(spawn_ids=[103], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[103]):
            # 맵 내 몬스터 한 무리를 죽이면
            return Event_06(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=110)
        self.set_interact_object(trigger_ids=[10000915], state=1) # 컨테이너를 반응 가능한 상태로 변경


class Event_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=111, text_id=25201901) # 수리공이 숨어있는 컨테이너를 찾으세요.

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000915], state=0):
            # 컨테이너를 반응 시키면
            return End(self.ctx) # 3번 반복하면 끝

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=111)
        self.spawn_monster(spawn_ids=[113], auto_target=False) # 그 안에 숨어있던 수리공 NPC들이 리젠
        self.set_dialogue(type=1, spawn_id=113, script='$52010009_QD__MAIN__2$', time=3, arg5=1)
        self.move_npc(spawn_id=113, patrol_name='MS2PatrolData0_1001')


class End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=701, type='trigger', achieve='findrepairman') # findrepairman


initial_state = idle
