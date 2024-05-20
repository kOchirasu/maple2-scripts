""" trigger/52000004_qd/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601])
        self.set_effect(trigger_ids=[602])
        self.destroy_monster(spawn_ids=[2001])
        self.destroy_monster(spawn_ids=[2099])
        self.destroy_monster(spawn_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016])
        self.set_portal(portal_id=2)
        self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005,3006,3007,3008,3009])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199]):
            return 던전시작(self.ctx)
        if not self.user_detected(box_ids=[199]):
            return 종료(self.ctx)


class 던전시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 차목표1(self.ctx)
        if not self.user_detected(box_ids=[199]):
            return 종료(self.ctx)


class 차목표1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601], visible=True)
        self.set_timer(timer_id='2', seconds=2)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3, script='$52000004_QD__MAIN__0$')
        self.set_skip(state=연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 카메라이동(self.ctx)


class 카메라이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)
        self.select_camera(trigger_id=301)
        self.set_skip(state=연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[602], visible=True)
        self.select_camera_path(path_ids=[301])
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[100]):
            return 피자들기(self.ctx)
        if not self.user_detected(box_ids=[199]):
            return 종료(self.ctx)


class 피자들기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)
        self.show_guide_summary(entity_id=25200401, text_id=25200401)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 엘리트스폰대기(self.ctx)
        if not self.user_detected(box_ids=[199]):
            return 종료(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=25200401)


class 엘리트스폰대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016], auto_target=False)
        self.set_effect(trigger_ids=[602])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 엘리트스폰(self.ctx)
        if not self.user_detected(box_ids=[199]):
            return 종료(self.ctx)


class 엘리트스폰(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=25200402, text_id=25200402)
        self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005,3006,3007,3008,3009], visible=True, fade=2.0)
        self.spawn_monster(spawn_ids=[2001], auto_target=False)
        self.set_dialogue(type=1, spawn_id=2001, script='$52000004_QD__MAIN__3$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 벽해제(self.ctx)
        if not self.user_detected(box_ids=[199]):
            return 종료(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=25200402)


class 벽해제(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005,3006,3007,3008,3009], fade=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[102]):
            return NPC등장(self.ctx)
        if not self.user_detected(box_ids=[199]):
            return 종료(self.ctx)


class NPC등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601])
        self.spawn_monster(spawn_ids=[2099], auto_target=False)
        self.set_dialogue(type=1, spawn_id=2099, script='$52000004_QD__MAIN__4$', time=3)
        self.move_npc(spawn_id=2099, patrol_name='MS2PatrolData_2099')
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[199]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='5'):
            return 미션성공(self.ctx)


class 미션성공(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[199], quest_ids=[10001852], quest_states=[2]):
            self.set_event_ui(type=7, arg2='$52000004_QD__MAIN__5$', arg3='3000', arg4='0')
            return 포털생성(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[10001851], quest_states=[2]):
            self.set_event_ui(type=7, arg2='$52000004_QD__MAIN__6$', arg3='3000', arg4='0')
            return 포털생성(self.ctx)
        if self.time_expired(timer_id='3'):
            return 포털생성(self.ctx)
        if not self.user_detected(box_ids=[199]):
            return 종료(self.ctx)


class 포털생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
            self.show_guide_summary(entity_id=25200403, text_id=25200403)
            return 종료대기(self.ctx)
        if not self.user_detected(box_ids=[199]):
            return 종료(self.ctx)


class 종료대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='30', seconds=30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='30'):
            self.move_user(map_id=2000166, portal_id=30, box_id=199)
            return 종료(self.ctx)
        if not self.user_detected(box_ids=[199]):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[2001])
        self.destroy_monster(spawn_ids=[2099])
        self.destroy_monster(spawn_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016])
        self.set_portal(portal_id=2)
        self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005,3006,3007,3008,3009])

    def on_tick(self) -> trigger_api.Trigger:
        return 대기(self.ctx)


initial_state = 대기
