""" trigger/52000021_qd/main01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6000]) # 보호막 이펙트
        self.set_effect(trigger_ids=[6100]) # 전투영역 배리어 룬 쉴드 이펙트
        self.set_effect(trigger_ids=[6200]) # 홀슈타트 아이스 쉴드 이펙트
        self.set_effect(trigger_ids=[6201]) # 홀슈타트 아이스 드라이브 이펙트
        self.set_effect(trigger_ids=[6202]) # 홀슈타트 아이스 임팩트 이펙트
        self.set_effect(trigger_ids=[6300]) # 이슈라 플레임 쉴드 이펙트
        self.set_effect(trigger_ids=[6301]) # 이슈라 플레임 드라이브 이펙트
        self.set_effect(trigger_ids=[6400]) # 보호막 불안정 연출 이펙트 Keep
        self.set_effect(trigger_ids=[6401]) # 보호막 불안정 연출 이펙트 Invoke
        self.set_effect(trigger_ids=[6500]) # 얼음 속성 공격 폭발 - 홀슈타트
        self.set_effect(trigger_ids=[6600]) # 얼음 속성 공격 그라운드 - 홀슈타트
        self.set_effect(trigger_ids=[6700]) # 얼음 속성 공격 인피니티 - 홀슈타트
        self.set_mesh(trigger_ids=[5000,5001,5002]) # 이슈라 영역 진입 제한
        self.set_mesh(trigger_ids=[4000,4001,4002,4003]) # 보호막 영역 탈출 제한
        self.set_interact_object(trigger_ids=[10000831], state=0) # 보호 룬 주문석 : Shield ON
        self.set_interact_object(trigger_ids=[10000832], state=2) # 보호 룬 주문석 : Shield OFF
        self.spawn_monster(spawn_ids=[111]) # 퀘스트용 유페리아
        self.spawn_monster(spawn_ids=[311]) # 퀘스트용 이슈라
        self.move_npc(spawn_id=311, patrol_name='MS2PatrolData_311') # 이슈라 Walking

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[60001030], quest_states=[1]):
            # 변절자를 쫓아서 진행 중 상태
            return 연출준비(self.ctx)


# 대치 상황 : 이슈라와 홀슈타트 Attack Idle 모션
class 연출준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[111]) # 퀘스트용 유페리아
        self.destroy_monster(spawn_ids=[311]) # 퀘스트용 이슈라
        self.set_timer(timer_id='1', seconds=2)
        self.set_mesh(trigger_ids=[5000,5001,5002], visible=True) # 이슈라 영역 진입 제한
        self.set_effect(trigger_ids=[6100], visible=True) # 전투영역 배리어 룬 쉴드 이펙트
        self.select_camera(trigger_id=600)
        self.spawn_monster(spawn_ids=[101]) # 연출용 유페리아
        self.spawn_monster(spawn_ids=[201]) # 연출용 홀슈타트
        self.spawn_monster(spawn_ids=[301]) # 연출용 이슈라
        self.set_effect(trigger_ids=[6200], visible=True) # 홀슈타트 아이스 쉴드 이펙트
        self.set_effect(trigger_ids=[6300], visible=True) # 이슈라 플레임 쉴드 이펙트
        self.set_effect(trigger_ids=[6201], visible=True) # 홀슈타트 아이스 드라이브 이펙트
        self.set_effect(trigger_ids=[6301], visible=True) # 이슈라 플레임 드라이브 이펙트
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 딜레이(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=1)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 카메라연출시작(self.ctx)


class 카메라연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=6)
        self.select_camera_path(path_ids=[600,601,602], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 이슈라대화01(self.ctx)


class 이슈라대화01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='4', seconds=5)
        self.set_dialogue(type=2, spawn_id=11001244, script='$52000021_QD__MAIN01__0$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return 이슈라대화02(self.ctx)


class 이슈라대화02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_dialogue(type=2, spawn_id=11001244, script='$52000021_QD__MAIN01__1$', time=5)
        self.set_interact_object(trigger_ids=[10000831], state=1) # 보호 룬 주문석 : Shield ON

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 주문석반응대기(self.ctx)


class 주문석반응대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=602, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000831], state=0):
            # 보호 룬 주문석 : Shield ON
            return 보호막설정01(self.ctx)

    def on_exit(self) -> None:
        self.set_interact_object(trigger_ids=[10000831], state=2) # 보호 룬 주문석 : Shield ON
        self.set_interact_object(trigger_ids=[10000832], state=0) # 보호 룬 주문석 : Shield OFF
        self.set_effect(trigger_ids=[6000], visible=True) # 보호막 이펙트
        self.set_mesh(trigger_ids=[4000,4001,4002,4003], visible=True) # 보호막 영역 탈출 제한


# 유저가 영역 안에 들어온 상태
class 보호막설정01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='10', seconds=1)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=603)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='10'):
            return 목표전달01(self.ctx)


class 목표전달01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='11', seconds=4)
        self.set_dialogue(type=2, spawn_id=11001244, script='$52000021_QD__MAIN01__2$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11'):
            return 목표전달02(self.ctx)


class 목표전달02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='12', seconds=2)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=603, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='12'):
            return 유저감지01(self.ctx)


class 유저감지01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9001]):
            return 탈출경고01(self.ctx)


class 탈출경고01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='20', seconds=4)
        self.set_dialogue(type=1, spawn_id=101, script='$52000021_QD__MAIN01__3$', time=2)
        self.set_dialogue(type=1, spawn_id=301, script='$52000021_QD__MAIN01__4$', time=3, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='20'):
            return 탈출경고02(self.ctx)


class 탈출경고02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='21', seconds=4)
        self.set_effect(trigger_ids=[6400], visible=True) # 보호막 불안정 연출 이펙트 Keep
        self.set_dialogue(type=1, spawn_id=301, script='$52000021_QD__MAIN01__5$', time=3, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='21'):
            return 탈출경고03(self.ctx)


class 탈출경고03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='22', seconds=4)
        self.set_dialogue(type=1, spawn_id=301, script='$52000021_QD__MAIN01__6$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='22'):
            return 탈출경고04(self.ctx)


class 탈출경고04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='25', seconds=3)
        self.set_effect(trigger_ids=[6401], visible=True) # 보호막 불안정 연출 이펙트 Invoke
        self.set_dialogue(type=1, spawn_id=101, script='$52000021_QD__MAIN01__7$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='25'):
            return 탈출경고05(self.ctx)


class 탈출경고05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='26', seconds=3)
        self.set_effect(trigger_ids=[6401], visible=True) # 보호막 불안정 연출 이펙트 Invoke
        self.set_dialogue(type=1, spawn_id=101, script='$52000021_QD__MAIN01__8$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='26'):
            return 탈출경고06(self.ctx)


class 탈출경고06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='26', seconds=3)
        self.set_dialogue(type=1, spawn_id=101, script='$52000021_QD__MAIN01__9$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='26'):
            return 탈출가능01(self.ctx)


class 탈출가능01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000832], state=1) # 보호 룬 주문석 : Shield OFF

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000832], state=0):
            # 보호 룬 주문석 : Shield OFF
            return 보호막해제01(self.ctx)

    def on_exit(self) -> None:
        self.set_interact_object(trigger_ids=[10000832], state=2) # 보호 룬 주문석 : Shield OFF


# 유저가 영역을 벗어남
class 보호막해제01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='30', seconds=1)
        self.set_effect(trigger_ids=[6000]) # 보호막 이펙트
        self.set_effect(trigger_ids=[6400]) # 보호막 불안정 연출 이펙트 Keep
        self.set_effect(trigger_ids=[6401]) # 보호막 불안정 연출 이펙트 Invoke
        self.set_effect(trigger_ids=[6202], visible=True) # 홀슈타트 아이스 임팩트 이펙트
        self.set_mesh(trigger_ids=[4000,4001,4002,4003]) # 보호막 영역 탈출 제한
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=610)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='30'):
            return 홀슈타트연출01(self.ctx)

    def on_exit(self) -> None:
        self.set_effect(trigger_ids=[6200]) # 홀슈타트 아이스 쉴드 이펙트
        self.set_effect(trigger_ids=[6201]) # 홀슈타트 아이스 드라이브 이펙트
        self.set_effect(trigger_ids=[6300]) # 이슈라 플레임 쉴드 이펙트
        self.set_effect(trigger_ids=[6301]) # 이슈라 플레임 드라이브 이펙트
        self.set_effect(trigger_ids=[6100]) # 전투영역 배리어 룬 쉴드 이펙트


class 홀슈타트연출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='31', seconds=2)
        self.set_effect(trigger_ids=[6202], visible=True) # 홀슈타트 아이스 임팩트 이펙트
        self.set_dialogue(type=2, spawn_id=11001244, script='$52000021_QD__MAIN01__10$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='31'):
            return 홀슈타트연출02(self.ctx)


class 홀슈타트연출02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='32', seconds=3)
        self.select_camera(trigger_id=611)
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_201')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9010, spawn_ids=[201]):
            return 홀슈타트연출03(self.ctx)


class 홀슈타트연출03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='33', seconds=1)
        self.set_effect(trigger_ids=[6700], visible=True) # 얼음 속성 공격 인피니티 - 홀슈타트
        self.set_effect(trigger_ids=[6600], visible=True) # 얼음 속성 공격 그라운드 - 홀슈타트
        self.set_effect(trigger_ids=[6500], visible=True) # 얼음 속성 공격 폭발 - 홀슈타트
        self.set_dialogue(type=2, spawn_id=11001244, script='$52000021_QD__MAIN01__11$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='33'):
            return 홀슈타트연출04(self.ctx)


class 홀슈타트연출04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='35', seconds=1)
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_202')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='35'):
            return 연출종료준비(self.ctx)


# 퀘스트용 NPC로 교체
class 연출종료준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='34', seconds=2)
        self.set_cinematic_ui(type=4)
        self.destroy_monster(spawn_ids=[201]) # 연출용 홀슈타트
        self.destroy_monster(spawn_ids=[101]) # 연출용 유페리아
        self.destroy_monster(spawn_ids=[301]) # 연출용 이슈라
        self.spawn_monster(spawn_ids=[111]) # 퀘스트용 유페리아
        self.spawn_monster(spawn_ids=[311]) # 퀘스트용 이슈라
        self.move_npc(spawn_id=311, patrol_name='MS2PatrolData_311') # 이슈라 Walking

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='34'):
            return 종료(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=4)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=611, enable=False)
        self.set_achievement(trigger_id=9900, type='trigger', achieve='EscapeHallstatt')
        self.set_mesh(trigger_ids=[5000,5001,5002]) # 이슈라 영역 진입 제한


initial_state = 대기
