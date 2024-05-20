""" trigger/52000015_qd/tutorial03.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000]) # 위험 연출 이펙트 01
        self.set_effect(trigger_ids=[5001]) # 위험 연출 이펙트 02
        self.set_effect(trigger_ids=[5002]) # 위험 연출 사운드 이펙트
        self.set_effect(trigger_ids=[6000]) # 이슈라 음성 사운드 이펙트 01
        self.set_effect(trigger_ids=[6001]) # 이슈라 음성 사운드 이펙트 02
        self.set_effect(trigger_ids=[6100]) # 변절한 칼리브 8검 음성 사운드 이펙트 01
        self.set_effect(trigger_ids=[6002]) # 이슈라 음성 사운드 이펙트 03
        self.set_effect(trigger_ids=[6003]) # 이슈라 음성 사운드 이펙트 04
        self.spawn_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[201])
        self.create_widget(type='Guide')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return 퀘스트진행중(self.ctx)


class 퀘스트진행중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[90000414], quest_states=[2]):
            # 레벨4 전투 퀘스트 완료 가능 상태인지 체크
            return 딜레이02(self.ctx)


class 딜레이02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 딜레이03(self.ctx)


class 딜레이03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_scene_skip(state=이슈라대화04대기CSkip, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        return 순간이동준비(self.ctx)


class 순간이동준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)
        self.set_effect(trigger_ids=[6000], visible=True) # 이슈라 음성 사운드 이펙트 01
        self.set_dialogue(type=2, spawn_id=11001244, script='$52000015_QD__TUTORIAL03__0$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 순간이동시작(self.ctx)


class 순간이동시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='4', seconds=2)
        self.set_cinematic_ui(type=4)
        self.destroy_monster(spawn_ids=[201])
        self.spawn_monster(spawn_ids=[202])
        self.move_user(map_id=52000015, portal_id=50, box_id=9001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return 순간이동진행(self.ctx)


class 순간이동진행(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=1)
        self.set_effect(trigger_ids=[6000]) # 이슈라 음성 사운드 이펙트 01

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 순간이동완료(self.ctx)


class 순간이동완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='6', seconds=3)
        self.select_camera(trigger_id=601)
        self.set_cinematic_ui(type=4)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='6'):
            return 적등장01(self.ctx)


class 적등장01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='7', seconds=2)
        self.spawn_monster(spawn_ids=[901])
        self.spawn_monster(spawn_ids=[902])
        self.spawn_monster(spawn_ids=[903])
        self.spawn_monster(spawn_ids=[904])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='7'):
            return 이슈라대화01(self.ctx)


class 이슈라대화01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='8', seconds=3)
        self.set_effect(trigger_ids=[6001], visible=True) # 이슈라 음성 사운드 이펙트 02
        self.set_dialogue(type=2, spawn_id=11001244, script='$52000015_QD__TUTORIAL03__1$', time=3)
        self.set_skip(state=이슈라대화02대기)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='8'):
            return 이슈라대화02대기(self.ctx)


class 이슈라대화02대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return 이슈라대화02(self.ctx)


class 이슈라대화02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='9', seconds=1)
        self.move_npc(spawn_id=901, patrol_name='MS2PatrolData_901')
        self.move_npc(spawn_id=902, patrol_name='MS2PatrolData_902')
        self.move_npc(spawn_id=903, patrol_name='MS2PatrolData_903')
        self.move_npc(spawn_id=904, patrol_name='MS2PatrolData_904')
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_101') # 레쟌 마중 시작

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='9'):
            return 변절자대화01(self.ctx)

    def on_exit(self) -> None:
        self.set_effect(trigger_ids=[6001]) # 이슈라 음성 사운드 이펙트 02


class 변절자대화01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='10', seconds=3)
        self.set_effect(trigger_ids=[6100], visible=True) # 변절한 칼리브 8검 음성 사운드 이펙트 01
        self.set_dialogue(type=2, spawn_id=11001235, script='$52000015_QD__TUTORIAL03__2$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='10'):
            return 이슈라대화03대기(self.ctx)


class 이슈라대화03대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return 이슈라대화03(self.ctx)


class 이슈라대화03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='11', seconds=3)
        self.set_effect(trigger_ids=[6100]) # 변절한 칼리브 8검 음성 사운드 이펙트 01
        self.set_effect(trigger_ids=[6002], visible=True) # 이슈라 음성 사운드 이펙트 03
        self.set_dialogue(type=2, spawn_id=11001244, script='$52000015_QD__TUTORIAL03__3$', time=3)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11'):
            return 이슈라대화04대기(self.ctx)


class 이슈라대화04대기CSkip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[202])
        self.move_user(map_id=52000015, portal_id=50, box_id=9001)
        self.remove_cinematic_talk()
        self.destroy_monster(spawn_ids=[901,902,903,904])

    def on_tick(self) -> trigger_api.Trigger:
        return 이슈라대화04(self.ctx)


class 이슈라대화04대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return 이슈라대화04(self.ctx)


class 이슈라대화04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=601, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        return HP가이드01(self.ctx)

    def on_exit(self) -> None:
        self.set_effect(trigger_ids=[6002]) # 이슈라 음성 사운드 이펙트 03


# HP 가칼이드
class HP가이드01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.guide_event(event_id=10012060) # 트리거 To가이드 : HP 가이드 시작

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='Guide', name='IsTriggerEvent') == 10012070:
            # 가이드 To 트리거  : HP 가이드 완료
            return 전투시작01(self.ctx)


class 전투시작01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[202])
        self.spawn_monster(spawn_ids=[203])
        self.destroy_monster(spawn_ids=[901,902,903,904])
        self.spawn_monster(spawn_ids=[911,912,913,914])

    def on_tick(self) -> trigger_api.Trigger:
        return 전투중01(self.ctx)


class 전투중01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='20', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='20'):
            return 위기상황연출준비(self.ctx)


class 위기상황연출준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='21', seconds=1)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_effect(trigger_ids=[5002], visible=True) # 위험 연출 사운드 이펙트
        self.set_effect(trigger_ids=[5000], visible=True) # 위험 연출 이펙트 01

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='21'):
            return 위기상황연출시작01(self.ctx)


class 위기상황연출시작01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='22', seconds=1)
        self.set_effect(trigger_ids=[5000], visible=True) # 위험 연출 이펙트 01
        self.set_effect(trigger_ids=[6003], visible=True) # 이슈라 음성 사운드 이펙트 04
        self.set_dialogue(type=2, spawn_id=11001244, script='$52000015_QD__TUTORIAL03__4$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='22'):
            return 위기상황연출시작02(self.ctx)


class 위기상황연출시작02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='23', seconds=1)
        self.set_effect(trigger_ids=[5000], visible=True) # 위험 연출 이펙트 01
        self.set_effect(trigger_ids=[5001], visible=True) # 위험 연출 이펙트 02

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='23'):
            return 위기상황연출완료(self.ctx)


class 위기상황연출완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.set_effect(trigger_ids=[5000], visible=True) # 위험 연출 이펙트 01
        self.set_effect(trigger_ids=[5001], visible=True) # 위험 연출 이펙트 02
        self.set_timer(timer_id='23', seconds=3)
        self.destroy_monster(spawn_ids=[203])
        self.destroy_monster(spawn_ids=[911,912,913,914])
        self.set_effect(trigger_ids=[6003]) # 이슈라 음성 사운드 이펙트 04

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='23'):
            return 위기상황종료(self.ctx)


class 위기상황종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000]) # 위험 연출 이펙트 01
        self.set_effect(trigger_ids=[5001]) # 위험 연출 이펙트 02
        self.move_user(map_id=63000012, portal_id=50, box_id=9002)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_exit(self) -> None:
        self.set_effect(trigger_ids=[5002]) # 위험 연출 사운드 이펙트


initial_state = 대기
