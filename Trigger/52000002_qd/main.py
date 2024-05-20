""" trigger/52000002_qd/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010])
        self.destroy_monster(spawn_ids=[2099])
        self.set_portal(portal_id=2)
        self.set_mesh(trigger_ids=[3000], visible=True)
        self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005,3006])
        self.set_mesh(trigger_ids=[3007,3008,3009,3010,3011,3012,3013], visible=True)
        self.set_interact_object(trigger_ids=[10000606], state=2)
        self.set_interact_object(trigger_ids=[10000607,10000608,10000609,10000610,10000611], state=2)
        self.set_interact_object(trigger_ids=[10000612,10000613,10000614,10000615,10000616], state=2)
        self.spawn_monster(spawn_ids=[1099], auto_target=False)
        self.spawn_monster(spawn_ids=[1101], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 던전시작(self.ctx)
        if not self.user_detected(box_ids=[101]):
            return 종료(self.ctx)


class 던전시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 차목표1(self.ctx)
        if not self.user_detected(box_ids=[101]):
            return 종료(self.ctx)


class 차목표1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3, script='$52000002_QD__MAIN__0$')
        self.set_timer(timer_id='5', seconds=5)
        self.set_skip(state=오브젝트생성)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 오브젝트생성(self.ctx)
        if not self.user_detected(box_ids=[101]):
            return 종료(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 오브젝트생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000607,10000608,10000609,10000610,10000611], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000607,10000608,10000609,10000610,10000611], state=0):
            return 단계준비2(self.ctx)
        if not self.user_detected(box_ids=[101]):
            return 종료(self.ctx)


class 단계준비2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)
        self.show_guide_summary(entity_id=25200202, text_id=25200202)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 레버대기(self.ctx)
        if not self.user_detected(box_ids=[101]):
            return 종료(self.ctx)


class 레버대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=25200202)
        self.set_interact_object(trigger_ids=[10000606], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000606], state=0):
            return 다리생성(self.ctx)
        if not self.user_detected(box_ids=[101]):
            return 종료(self.ctx)


class 다리생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3000])
        self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005,3006], visible=True, interval=300, fade=3.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[104]):
            return 단계시작2(self.ctx)
        if not self.user_detected(box_ids=[101]):
            return 종료(self.ctx)


class 단계시작2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3, script='$52000002_QD__MAIN__2$')
        self.set_timer(timer_id='5', seconds=5)
        self.set_skip(state=양생성)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 양생성(self.ctx)
        if not self.user_detected(box_ids=[101]):
            return 종료(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 양생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000612,10000613,10000614,10000615,10000616], state=1)
        self.spawn_monster(spawn_ids=[2001,2002,2003,2004,2005], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000612,10000613,10000614,10000615,10000616], state=2):
            return 단계준비3(self.ctx)
        if not self.user_detected(box_ids=[101]):
            return 종료(self.ctx)


class 단계준비3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=2)
        self.show_guide_summary(entity_id=25200202, text_id=25200202)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 단계대기3(self.ctx)
        if not self.user_detected(box_ids=[101]):
            return 종료(self.ctx)


class 단계대기3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=25200202)
        self.set_mesh(trigger_ids=[3007,3008,3009,3010,3011,3012,3013], interval=200, fade=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[106]):
            return 단계시작3(self.ctx)
        if not self.user_detected(box_ids=[101]):
            return 종료(self.ctx)


class 단계시작3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3, script='$52000002_QD__MAIN__4$')
        self.set_timer(timer_id='5', seconds=5)
        self.set_skip(state=늑대생성)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 늑대생성(self.ctx)
        if not self.user_detected(box_ids=[101]):
            return 종료(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 늑대생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2006,2007,2008,2009,2010], auto_target=False)
        self.spawn_monster(spawn_ids=[2099], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2099]):
            return 성공대기(self.ctx)
        if not self.user_detected(box_ids=[101]):
            return 종료(self.ctx)


class 성공대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[101]):
            return 종료(self.ctx)
        if self.time_expired(timer_id='2'):
            return 미션성공(self.ctx)


class 미션성공(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1102], auto_target=False)
        self.move_npc(spawn_id=1102, patrol_name='MS2PatrolData_1102')
        self.set_event_ui(type=7, arg2='$52000002_QD__MAIN__5$', arg3='3000', arg4='0')
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 포털생성(self.ctx)
        if not self.user_detected(box_ids=[101]):
            return 종료(self.ctx)


class 포털생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=1102, script='$52000002_QD__MAIN__6$', time=6)
        self.set_timer(timer_id='30', seconds=30)
        self.show_guide_summary(entity_id=25200203, text_id=25200203)
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='30'):
            self.move_user(map_id=2000002, portal_id=30, box_id=101)
            return 종료(self.ctx)
        if not self.user_detected(box_ids=[101]):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=25200203)
        self.hide_guide_summary(entity_id=25200202)
        self.destroy_monster(spawn_ids=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010])
        self.destroy_monster(spawn_ids=[2099])
        self.destroy_monster(spawn_ids=[1099])
        self.destroy_monster(spawn_ids=[1101])
        self.destroy_monster(spawn_ids=[1102])
        self.set_portal(portal_id=2)
        self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005,3006])
        self.set_interact_object(trigger_ids=[10000606], state=2)
        self.set_interact_object(trigger_ids=[10000607,10000608,10000609,10000610,10000611], state=2)
        self.set_interact_object(trigger_ids=[10000612,10000613,10000614,10000615,10000616], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        return 대기(self.ctx)


initial_state = 대기
