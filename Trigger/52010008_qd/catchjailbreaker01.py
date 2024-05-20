""" trigger/52010008_qd/catchjailbreaker01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[901,902,903,904,905,906], auto_target=False)
        self.set_interact_object(trigger_ids=[10000851], state=0)
        self.set_mesh(trigger_ids=[6000], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return 딜레이01(self.ctx)


class 딜레이01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='10', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='10'):
            return 전투안내01(self.ctx)


class 전투안내01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=100, text_id=40010) # 적을 모두 처치하세요

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[901,902,903,904,905,906]):
            return 죄수찾기01(self.ctx)


class 죄수찾기01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=100)
        self.set_interact_object(trigger_ids=[10000851], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000851], state=0):
            return 죄수등장01(self.ctx)


class 죄수등장01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[6000])
        self.set_timer(timer_id='11', seconds=1)
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_1010')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11'):
            return 죄수등장02(self.ctx)


class 죄수등장02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='12', seconds=2)
        self.spawn_monster(spawn_ids=[201], auto_target=False)
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_2010')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='12'):
            return 벨마등장01(self.ctx)


class 벨마등장01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='20', seconds=1)
        self.spawn_monster(spawn_ids=[301], auto_target=False)
        self.select_camera(trigger_id=601)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='20'):
            return 벨마대화01(self.ctx)


class 벨마대화01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='21', seconds=3)
        self.set_dialogue(type=2, spawn_id=11000521, script='$52010008_QD__CATCHJAILBREAKER01__0$', time=3)
        self.set_skip(state=벨마대화02대기)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='21'):
            return 벨마대화02대기(self.ctx)


class 벨마대화02대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return 벨마대화02(self.ctx)


class 벨마대화02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='22', seconds=3)
        self.set_dialogue(type=2, spawn_id=11000521, script='$52010008_QD__CATCHJAILBREAKER01__1$', time=3)
        self.set_skip(state=벨마대화03대기)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='22'):
            return 벨마대화03대기(self.ctx)


class 벨마대화03대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return 벨마대화03(self.ctx)


class 벨마대화03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='23', seconds=3)
        self.set_dialogue(type=2, spawn_id=11000521, script='$52010008_QD__CATCHJAILBREAKER01__2$', time=3)
        self.set_skip(state=벨마연출종료01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='23'):
            return 벨마연출종료01(self.ctx)


class 벨마연출종료01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_timer(timer_id='30', seconds=1)
        self.select_camera(trigger_id=601, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_achievement(trigger_id=9000, type='trigger', achieve='catchjailbreaker')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='30'):
            return 유저이동준비(self.ctx)


class 유저이동준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='31', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='31'):
            return 유저이동시작(self.ctx)


class 유저이동시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2010019, portal_id=2, box_id=9000)
        self.destroy_monster(spawn_ids=[101,201,301])
        self.destroy_monster(spawn_ids=[901,902,903,904,905,906])


initial_state = 대기
