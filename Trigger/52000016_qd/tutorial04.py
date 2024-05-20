""" trigger/52000016_qd/tutorial04.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[10000], visible=True) # 입구 길막기
        self.set_agent(trigger_ids=[10001], visible=True) # 입구 길막기
        self.set_agent(trigger_ids=[10002], visible=True) # 입구 길막기
        self.set_agent(trigger_ids=[10003], visible=True) # 입구 길막기
        self.set_agent(trigger_ids=[10004], visible=True) # 입구 길막기
        self.set_agent(trigger_ids=[10005], visible=True) # 입구 길막기
        self.set_agent(trigger_ids=[10010], visible=True) # 입구 길막기
        self.set_agent(trigger_ids=[10006], visible=True) # 다리 길막기
        self.set_agent(trigger_ids=[10007], visible=True) # 다리 길막기
        self.set_agent(trigger_ids=[10008], visible=True) # 다리 길막기
        self.set_agent(trigger_ids=[10009], visible=True) # 다리 길막기
        self.set_effect(trigger_ids=[6000]) # 가이드 서머리 알림 사운드
        self.set_effect(trigger_ids=[7000]) # 먼지
        self.set_effect(trigger_ids=[7001]) # 먼지
        self.set_effect(trigger_ids=[7002]) # 먼지
        self.set_effect(trigger_ids=[7003]) # 먼지
        self.set_effect(trigger_ids=[7004]) # 먼지
        self.set_effect(trigger_ids=[7005]) # 먼지
        self.set_effect(trigger_ids=[7006]) # 먼지
        self.set_effect(trigger_ids=[7007]) # 먼지
        self.set_effect(trigger_ids=[7010]) # 동굴 입구 흔들림
        self.set_effect(trigger_ids=[7020]) # 동굴 입구 무너지는 소리
        self.set_effect(trigger_ids=[7011]) # 다리 생길 때 흔들림
        self.set_effect(trigger_ids=[7021]) # 다리 나타날 때 효과음
        self.set_effect(trigger_ids=[7030]) # 레버 장치에서 들리는 소리
        self.set_effect(trigger_ids=[7040]) # 전투 연출에서 룬 쉴드 이펙트 소리
        self.set_effect(trigger_ids=[7050]) # 전투 연출에서 공격 스킬 이펙트 소리 NEW
        self.set_skill(trigger_ids=[910]) # 입구 큐브 부수기 스킬
        self.set_skill(trigger_ids=[911]) # 입구 큐브 부수기 스킬
        self.set_skill(trigger_ids=[912]) # 입구 큐브 부수기 스킬
        self.set_skill(trigger_ids=[913]) # 입구 큐브 부수기 스킬
        self.set_skill(trigger_ids=[914]) # 입구 큐브 부수기 스킬
        self.set_mesh(trigger_ids=[2000], visible=True) # PCProtect barrier ON
        self.set_mesh(trigger_ids=[3000], visible=True) # invisible barrier ON
        self.set_mesh(trigger_ids=[3001], visible=True) # bridge barrier ON
        self.set_mesh(trigger_ids=[4000,4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4014,4015]) # Rock  Visible OFF
        self.set_mesh(trigger_ids=[4020,4021,4022,4023,4024,4025,4026,4027]) # Bridge  Visible OFF
        self.set_interact_object(trigger_ids=[10000825], state=0) # 기관 작동 레버
        self.set_portal(portal_id=2)
        self.set_effect(trigger_ids=[8200]) # 이슈라 플레임 쉴드 이펙트
        self.set_effect(trigger_ids=[8300]) # 홀슈타트 아이스 쉴드 이펙트
        self.set_effect(trigger_ids=[8201]) # 이슈라 플레임 임팩트 이펙트
        self.set_effect(trigger_ids=[8301]) # 홀슈타트 아이스 임팩트 이펙트
        self.set_effect(trigger_ids=[8202]) # 이슈라 플레임 그라운드 이펙트
        self.set_effect(trigger_ids=[8302]) # 홀슈타트 아이스 그라운드 이펙트
        self.set_effect(trigger_ids=[8203]) # 이슈라 플레임 인피니티 이펙트
        self.set_effect(trigger_ids=[8303]) # 홀슈타트 아이스 인피니티 이펙트
        self.set_effect(trigger_ids=[8000]) # 싸울 때 흔들림
        self.set_effect(trigger_ids=[6100]) # 척후병 시네마틱 음성 01 사운드
        self.set_effect(trigger_ids=[6101]) # 척후병 시네마틱 음성 02 사운드
        self.set_effect(trigger_ids=[6102]) # 척후병 시네마틱 음성 03 사운드
        self.set_effect(trigger_ids=[6103]) # 척후병 시네마틱 음성 04 사운드
        self.set_effect(trigger_ids=[6104]) # 척후병 시네마틱 음성 05 사운드
        self.set_effect(trigger_ids=[6105]) # 척후병 시네마틱 음성 06 사운드
        self.set_effect(trigger_ids=[6106]) # 척후병 시네마틱 음성 06 사운드
        self.set_effect(trigger_ids=[6200]) # 이슈라 시네마틱 음성 01 사운드
        self.set_effect(trigger_ids=[6201]) # 이슈라 시네마틱 음성 02 사운드
        self.set_effect(trigger_ids=[6202]) # 이슈라 시네마틱 음성 03 사운드
        self.set_effect(trigger_ids=[6203]) # 이슈라 시네마틱 음성 04 사운드
        self.set_effect(trigger_ids=[6210]) # 홀슈타트 시네마틱 음성 01 사운드
        self.set_effect(trigger_ids=[6211]) # 홀슈타트 시네마틱 음성 02 사운드
        self.set_effect(trigger_ids=[6212]) # 홀슈타트 시네마틱 음성 03 사운드
        self.set_effect(trigger_ids=[6300]) # 렌듀비앙 시네마틱 음성 01 사운드
        self.set_effect(trigger_ids=[6301]) # 렌듀비앙 시네마틱 음성 02 사운드
        self.set_effect(trigger_ids=[6302]) # 렌듀비앙 시네마틱 음성 03 사운드
        self.set_effect(trigger_ids=[6400]) # 이슈라 시네마틱 음성 05 사운드
        self.set_effect(trigger_ids=[6401]) # 이슈라 시네마틱 음성 06 사운드
        self.set_effect(trigger_ids=[6402]) # 이슈라 시네마틱 음성 07 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[90000417], quest_states=[1]):
            return 딜레이01(self.ctx)


class 딜레이01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_random_mesh(trigger_ids=[4000,4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4014,4015], visible=True, start_delay=16, interval=50, fade=80) # Rock Visible  ON

    def on_tick(self) -> trigger_api.Trigger:
        return 막힌길발견01(self.ctx)


class 막힌길발견01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=601)

    def on_tick(self) -> trigger_api.Trigger:
        return 딜레이02(self.ctx)


class 딜레이02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[910], enable=True) # 입구 큐브 부수기 스킬
        self.set_skill(trigger_ids=[911], enable=True) # 입구 큐브 부수기 스킬
        self.set_skill(trigger_ids=[912], enable=True) # 입구 큐브 부수기 스킬
        self.set_skill(trigger_ids=[913], enable=True) # 입구 큐브 부수기 스킬
        self.set_skill(trigger_ids=[914], enable=True) # 입구 큐브 부수기 스킬
        self.set_effect(trigger_ids=[7010], visible=True) # 동굴 입구 흔들림
        self.set_effect(trigger_ids=[7020], visible=True) # 동굴 입구 무너지는 소리

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 막힌길발견02(self.ctx)


class 막힌길발견02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=4)
        self.set_effect(trigger_ids=[7000], visible=True) # 먼지
        self.set_effect(trigger_ids=[7001], visible=True) # 먼지
        self.set_effect(trigger_ids=[7002], visible=True) # 먼지
        self.set_effect(trigger_ids=[7003], visible=True) # 먼지
        self.set_effect(trigger_ids=[7004], visible=True) # 먼지
        self.set_effect(trigger_ids=[7005], visible=True) # 먼지
        self.set_effect(trigger_ids=[7006], visible=True) # 먼지
        self.set_effect(trigger_ids=[7007], visible=True) # 먼지

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 척후병입장(self.ctx)

    def on_exit(self) -> None:
        self.set_mesh(trigger_ids=[2000]) # PCProtect barrier ON


class 척후병입장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)
        self.spawn_monster(spawn_ids=[101])
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_1000')
        self.set_effect(trigger_ids=[6100], visible=True) # 척후병 시네마틱 음성 01 사운드
        self.set_dialogue(type=2, spawn_id=11001249, script='$52000016_QD__TUTORIAL04__0$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 돌치우기안내01(self.ctx)


class 돌치우기안내01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=3)
        self.set_effect(trigger_ids=[6101], visible=True) # 척후병 시네마틱 음성 02 사운드
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_1001')
        self.set_dialogue(type=2, spawn_id=11001249, script='$52000016_QD__TUTORIAL04__1$', time=3)
        self.set_skip(state=돌치우기안내03)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 돌치우기안내03(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()
        self.set_effect(trigger_ids=[7010]) # 동굴 입구 흔들림
        self.set_effect(trigger_ids=[7020]) # 동굴 입구 무너지는 소리
        self.set_skill(trigger_ids=[910]) # 입구 큐브 부수기 스킬
        self.set_skill(trigger_ids=[911]) # 입구 큐브 부수기 스킬
        self.set_skill(trigger_ids=[912]) # 입구 큐브 부수기 스킬
        self.set_skill(trigger_ids=[913]) # 입구 큐브 부수기 스킬
        self.set_skill(trigger_ids=[914]) # 입구 큐브 부수기 스킬


class 돌치우기안내03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=601, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        return 첫번째돌들기가이드01(self.ctx)


class 첫번째돌들기가이드01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6000], visible=True) # 가이드 서머리 알림 사운드
        self.show_guide_summary(entity_id=10014010, text_id=10014010) # 가이드 : 스페이스 키를 눌러 바위덩이 들기

    def on_tick(self) -> trigger_api.Trigger:
        if not self.detect_liftable_object(box_ids=[9001], item_id=30000440):
            # 1번 박스에서 1번돌이 없어지면
            return 첫번째돌놓기01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=10014010)


class 첫번째돌놓기01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6000], visible=True) # 가이드 서머리 알림 사운드
        # 가이드 : 스페이스 키를 눌러 눌러 바위덩이  내려놓기
        self.show_guide_summary(entity_id=10014020, text_id=10014020)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9011,9012], item_id=30000440):
            # 1번 돌을 타겟 박스에 놓으면
            return 척후병이동01(self.ctx)


class 척후병이동01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=10014020)
        self.spawn_monster(spawn_ids=[901,902,903,904,905,906,907], auto_target=False)
        self.set_random_mesh(trigger_ids=[4000,4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4014,4015], start_delay=16, interval=100, fade=80) # Rock Visible  OFF
        self.set_mesh(trigger_ids=[3000]) # invisible barrier OFF
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_1002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9004, spawn_ids=[101]):
            return 척후병이동02(self.ctx)


class 척후병이동02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=101, script='$52000016_QD__TUTORIAL04__2$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9005, spawn_ids=[101]):
            return 척후병전투시작01(self.ctx)


class 척후병전투시작01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='9', seconds=1)
        self.set_agent(trigger_ids=[10000]) # 입구 길막기
        self.set_agent(trigger_ids=[10001]) # 입구 길막기
        self.set_agent(trigger_ids=[10002]) # 입구 길막기
        self.set_agent(trigger_ids=[10003]) # 입구 길막기
        self.set_agent(trigger_ids=[10004]) # 입구 길막기
        self.set_agent(trigger_ids=[10005]) # 입구 길막기
        self.set_agent(trigger_ids=[10010]) # 입구 길막기

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='9'):
            return 전투중01(self.ctx)


class 전투중01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='10', seconds=2)
        self.set_dialogue(type=1, spawn_id=101, script='$52000016_QD__TUTORIAL04__3$', time=2)
        self.set_effect(trigger_ids=[6102], visible=True) # 척후병 시네마틱 음성 03 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='10'):
            return 전투중02(self.ctx)


class 전투중02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=101, script='$52000016_QD__TUTORIAL04__4$', time=2)
        self.set_effect(trigger_ids=[6000], visible=True) # 가이드 서머리 알림 사운드
        self.show_guide_summary(entity_id=10014030, text_id=10014030) # 가이드 : 주변 몬스터 모두 처치하기

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[901,902,903,904,905,906,907]):
            return 전투종료01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=10014030)


class 전투종료01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='11', seconds=2)
        self.set_effect(trigger_ids=[6103], visible=True) # 척후병 시네마틱 음성 04 사운드
        self.set_dialogue(type=1, spawn_id=101, script='$52000016_QD__TUTORIAL04__5$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11'):
            return 전투종료02(self.ctx)


class 전투종료02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='12', seconds=2)
        self.set_dialogue(type=1, spawn_id=101, script='$52000016_QD__TUTORIAL04__6$', time=2)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_1003')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='12'):
            return 다리로이동01(self.ctx)


class 다리로이동01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9006, spawn_ids=[101]):
            return 연출준비01(self.ctx)


class 연출준비01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='13', seconds=3)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=602)
        self.set_dialogue(type=2, spawn_id=11001249, script='$52000016_QD__TUTORIAL04__7$', time=3)
        self.set_effect(trigger_ids=[6104], visible=True) # 척후병 시네마틱 음성 05 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='13'):
            return 연출준비02(self.ctx)


class 연출준비02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='14', seconds=2)
        self.set_dialogue(type=2, spawn_id=11001249, script='$52000016_QD__TUTORIAL04__8$', time=2)
        self.set_effect(trigger_ids=[6105], visible=True) # 척후병 시네마틱 음성 06 사운드
        self.spawn_monster(spawn_ids=[201]) # 연출용 이슈라
        self.spawn_monster(spawn_ids=[301]) # 연출용 홀슈타트
        self.spawn_monster(spawn_ids=[210,211,212,213,214,215,216,217]) # 연출용 아군8
        self.spawn_monster(spawn_ids=[310,311,312,313]) # 연출용 아군4
        # self.set_skip(state=연출시작01대기)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='14'):
            return 연출시작01대기(self.ctx)


class 연출시작01대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return 연출시작01(self.ctx)


class 연출시작01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=연출종료01_skip, action='nextState')
        self.set_timer(timer_id='16', seconds=1)
        self.select_camera_path(path_ids=[602,603], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='16'):
            return 대결연출01(self.ctx)


class 대결연출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='18', seconds=3)
        self.set_dialogue(type=2, spawn_id=11001244, script='$52000016_QD__TUTORIAL04__9$', time=3)
        self.set_effect(trigger_ids=[6200], visible=True) # 이슈라 시네마틱 음성 01 사운드
        self.destroy_monster(spawn_ids=[101]) # 전투용 척후병 삭제
        self.spawn_monster(spawn_ids=[102]) # 연출용 척후병 생성
        self.set_skip(state=대결연출02대기)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='18'):
            return 대결연출02대기(self.ctx)


class 대결연출02대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return 대결연출02(self.ctx)


class 대결연출02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='19', seconds=7)
        self.set_dialogue(type=2, spawn_id=11001231, script='$52000016_QD__TUTORIAL04__10$', time=6)
        self.set_effect(trigger_ids=[6200]) # 이슈라 시네마틱 음성 01 사운드
        self.set_effect(trigger_ids=[6210], visible=True) # 홀슈타트 시네마틱 음성 01 사운드
        self.set_skip(state=대결연출03대기)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='19'):
            return 대결연출03대기(self.ctx)


class 대결연출03대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return 대결연출03(self.ctx)


class 대결연출03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='20', seconds=5)
        self.set_dialogue(type=2, spawn_id=11001244, script='$52000016_QD__TUTORIAL04__11$', time=4)
        self.set_effect(trigger_ids=[6210]) # 홀슈타트 시네마틱 음성 01 사운드
        self.set_effect(trigger_ids=[6201], visible=True) # 이슈라 시네마틱 음성 02 사운드
        self.set_skip(state=대결연출04대기)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='20'):
            return 대결연출04대기(self.ctx)


class 대결연출04대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return 대결연출04(self.ctx)


class 대결연출04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='21', seconds=5)
        self.set_dialogue(type=2, spawn_id=11001231, script='$52000016_QD__TUTORIAL04__12$', time=5)
        self.set_effect(trigger_ids=[6201]) # 이슈라 시네마틱 음성 02 사운드
        self.set_effect(trigger_ids=[6211], visible=True) # 홀슈타트 시네마틱 음성 02 사운드
        self.set_skip(state=대결연출05대기)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='21'):
            return 대결연출05대기(self.ctx)


class 대결연출05대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return 대결연출05(self.ctx)


class 대결연출05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='22', seconds=4)
        self.set_dialogue(type=2, spawn_id=11001244, script='$52000016_QD__TUTORIAL04__13$', time=3)
        self.set_effect(trigger_ids=[6211]) # 홀슈타트 시네마틱 음성 02 사운드
        self.set_effect(trigger_ids=[6202], visible=True) # 이슈라 시네마틱 음성 03 사운드
        self.set_skip(state=대결연출06대기)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='22'):
            return 대결연출06대기(self.ctx)


class 대결연출06대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return 대결연출06(self.ctx)


class 대결연출06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='23', seconds=4)
        self.set_dialogue(type=2, spawn_id=11001231, script='$52000016_QD__TUTORIAL04__14$', time=3)
        self.set_effect(trigger_ids=[6202]) # 이슈라 시네마틱 음성 03 사운드
        self.set_effect(trigger_ids=[6212], visible=True) # 홀슈타트 시네마틱 음성 03 사운드
        self.set_skip(state=대결연출07대기)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='23'):
            return 대결연출07대기(self.ctx)


class 대결연출07대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 대결연출07(self.ctx)


class 대결연출07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='24', seconds=1)
        self.select_camera(trigger_id=606)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='24'):
            return 대결연출08(self.ctx)


class 대결연출08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='25', seconds=1)
        self.set_effect(trigger_ids=[7050], visible=True) # 전투 연출에서 공격 스킬 이펙트 소리 NEW
        self.set_dialogue(type=2, spawn_id=11001244, script='$52000016_QD__TUTORIAL04__15$', time=2)
        self.set_effect(trigger_ids=[6212]) # 홀슈타트 시네마틱 음성 03 사운드
        self.set_effect(trigger_ids=[6203], visible=True) # 이슈라 시네마틱 음성 04 사운드
        self.set_effect(trigger_ids=[8200], visible=True) # 이슈라 플레임 쉴드 이펙트
        self.set_effect(trigger_ids=[8300], visible=True) # 홀슈타트 아이스 쉴드 이펙트
        # self.set_effect(trigger_ids=[7040], visible=True) # 전투 연출에서 룬 쉴드 이펙트 소리

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='25'):
            return 이펙트연출01(self.ctx)


class 이펙트연출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='26', seconds=2)
        self.set_effect(trigger_ids=[8201], visible=True) # 이슈라 플레임 임팩트 이펙트
        self.set_effect(trigger_ids=[8301], visible=True) # 홀슈타트 아이스 임팩트 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='26'):
            return 이펙트연출02(self.ctx)

    def on_exit(self) -> None:
        self.set_effect(trigger_ids=[8200]) # 이슈라 플레임 쉴드 이펙트
        self.set_effect(trigger_ids=[8300]) # 홀슈타트 아이스 쉴드 이펙트


class 이펙트연출02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='27', seconds=1)
        self.set_effect(trigger_ids=[8201]) # 이슈라 플레임 임팩트 이펙트
        self.set_effect(trigger_ids=[8301]) # 홀슈타트 아이스 임팩트 이펙트
        self.set_effect(trigger_ids=[8000], visible=True) # 싸울 때 흔들림
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_2100')
        self.move_npc(spawn_id=301, patrol_name='MS2PatrolData_3100')
        self.set_effect(trigger_ids=[8203], visible=True) # 이슈라 플레임 인피니티 이펙트
        self.set_effect(trigger_ids=[8303], visible=True) # 홀슈타트 아이스 인피니티 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='27'):
            return 이펙트연출03(self.ctx)


class 이펙트연출03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='28', seconds=1)
        self.set_effect(trigger_ids=[8202], visible=True) # 이슈라 플레임 그라운드 이펙트
        self.set_effect(trigger_ids=[8302], visible=True) # 홀슈타트 아이스 그라운드 이펙트
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='28'):
            return 연출종료01(self.ctx)


class 연출종료01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='30', seconds=1)
        self.set_cinematic_ui(type=4)
        self.select_camera(trigger_id=606, enable=False)
        self.select_camera(trigger_id=602, enable=False)
        self.select_camera(trigger_id=603, enable=False)
        self.set_effect(trigger_ids=[8203]) # 이슈라 플레임 인피니티 이펙트
        self.set_effect(trigger_ids=[8303]) # 홀슈타트 아이스 인피니티 이펙트
        self.set_effect(trigger_ids=[8202]) # 이슈라 플레임 그라운드 이펙트
        self.set_effect(trigger_ids=[8302]) # 홀슈타트 아이스 그라운드 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='30'):
            return 레버당기기01(self.ctx)

    def on_exit(self) -> None:
        self.set_effect(trigger_ids=[7040]) # 전투 연출에서 룬 쉴드 이펙트 소리
        self.set_effect(trigger_ids=[7050]) # 전투 연출에서 공격 스킬 이펙트 소리 NEW
        self.set_effect(trigger_ids=[8000]) # 싸울 때 흔들림


class 연출종료01_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101]) # 전투용 척후병 삭제
        self.destroy_monster(spawn_ids=[102]) # 연출용 척후병 삭제
        self.remove_cinematic_talk()
        self.set_timer(timer_id='30', seconds=1)
        self.spawn_monster(spawn_ids=[102]) # 연출용 척후병 생성
        self.set_cinematic_ui(type=4)
        self.select_camera(trigger_id=606, enable=False)
        self.select_camera(trigger_id=602, enable=False)
        self.select_camera(trigger_id=603, enable=False)
        self.set_effect(trigger_ids=[8203]) # 이슈라 플레임 인피니티 이펙트
        self.set_effect(trigger_ids=[8303]) # 홀슈타트 아이스 인피니티 이펙트
        self.set_effect(trigger_ids=[8202]) # 이슈라 플레임 그라운드 이펙트
        self.set_effect(trigger_ids=[8302]) # 홀슈타트 아이스 그라운드 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='30'):
            return 레버당기기01(self.ctx)

    def on_exit(self) -> None:
        self.set_effect(trigger_ids=[7040]) # 전투 연출에서 룬 쉴드 이펙트 소리
        self.set_effect(trigger_ids=[7050]) # 전투 연출에서 공격 스킬 이펙트 소리 NEW
        self.set_effect(trigger_ids=[8000]) # 싸울 때 흔들림


class 레버당기기01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='31', seconds=1)
        self.set_cinematic_ui(type=4)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=605)
        self.set_interact_object(trigger_ids=[10000825], state=1) # 기관 작동 레버
        self.set_effect(trigger_ids=[7030], visible=True) # 레버 장치에서 들리는 소리

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='31'):
            return 레버당기기02(self.ctx)


class 레버당기기02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='35', seconds=3)
        self.set_dialogue(type=2, spawn_id=11001249, script='$52000016_QD__TUTORIAL04__16$', time=3)
        self.set_effect(trigger_ids=[6106], visible=True) # 척후병 시네마틱 음성 06 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='35'):
            return 다리만들기01(self.ctx)

    def on_exit(self) -> None:
        self.set_effect(trigger_ids=[6000], visible=True) # 가이드 서머리 알림 사운드
        self.show_guide_summary(entity_id=10014031, text_id=10014031) # 가이드 : 레버 작동시키기


class 다리만들기01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=605, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawn_ids=[301]) # 연출용 홀슈타트
        self.destroy_monster(spawn_ids=[210,211,212,213,214,215,216,217]) # 연출용 아군8
        self.destroy_monster(spawn_ids=[310,311,312,313]) # 연출용 아군4
        self.spawn_monster(spawn_ids=[220,221,222,223,224,225,226,227]) # 쓰러진 연출용 아군4
        self.set_effect(trigger_ids=[7030]) # 레버 장치에서 들리는 소리

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000825], state=0):
            # 기관 작동 레버
            return 다리만들기02(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=10014031)


class 다리만들기02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='40', seconds=1)
        self.set_random_mesh(trigger_ids=[4020,4021,4022,4023,4024,4025,4026,4027], visible=True, start_delay=8, interval=120, fade=120) # Bridge Visible  ON
        self.set_effect(trigger_ids=[7011], visible=True) # 다리 생길 때 흔들림
        self.set_effect(trigger_ids=[7021], visible=True) # 다리 나타날 때 효과음
        self.set_agent(trigger_ids=[10006]) # 다리 길막기
        self.set_agent(trigger_ids=[10007]) # 다리 길막기
        self.set_agent(trigger_ids=[10008]) # 다리 길막기
        self.set_agent(trigger_ids=[10009]) # 다리 길막기
        self.set_effect(trigger_ids=[6000], visible=True) # 가이드 서머리 알림 사운드
        self.show_guide_summary(entity_id=10014032, text_id=10014032) # 가이드 : 다리 건너가기
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_2000')
        self.set_mesh(trigger_ids=[3001]) # bridge barrier OFF

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='40'):
            return 다리건너기01(self.ctx)


class 다리건너기01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_1004')
        self.change_monster(from_spawn_id=201, to_spawn_id=202)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9020, spawn_ids=[102]):
            return 다리건너기02(self.ctx)


class 다리건너기02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9021]):
            return 마무리준비01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=10014032)


class 마무리준비01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='41', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='41'):
            return 마무리연출01(self.ctx)


class 마무리연출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='42', seconds=1)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=604)
        self.set_scene_skip(state=마무리연출08, action='nextState')
        self.spawn_monster(spawn_ids=[401])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='42'):
            return 마무리연출02(self.ctx)


class 마무리연출02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='43', seconds=3)
        self.move_npc(spawn_id=401, patrol_name='MS2PatrolData_4000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='43'):
            return 마무리연출03(self.ctx)


class 마무리연출03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='44', seconds=3)
        self.set_dialogue(type=2, spawn_id=11001230, script='$52000016_QD__TUTORIAL04__17$', time=3)
        self.set_effect(trigger_ids=[6300], visible=True) # 렌듀비앙 시네마틱 음성 01 사운드
        self.set_skip(state=마무리연출04대기)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='44'):
            return 마무리연출04대기(self.ctx)


class 마무리연출04대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return 마무리연출04(self.ctx)


class 마무리연출04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='45', seconds=5)
        self.set_effect(trigger_ids=[6300]) # 렌듀비앙 시네마틱 음성 01 사운드
        self.set_dialogue(type=2, spawn_id=11001244, script='$52000016_QD__TUTORIAL04__18$', time=4)
        self.set_effect(trigger_ids=[6400], visible=True) # 이슈라 시네마틱 음성 05 사운드
        self.set_skip(state=마무리연출05대기)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='45'):
            return 마무리연출05대기(self.ctx)


class 마무리연출05대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return 마무리연출05(self.ctx)


class 마무리연출05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='46', seconds=5)
        self.set_effect(trigger_ids=[6400]) # 이슈라 시네마틱 음성 05 사운드
        self.set_dialogue(type=2, spawn_id=11001230, script='$52000016_QD__TUTORIAL04__19$', time=4)
        self.set_effect(trigger_ids=[6301], visible=True) # 렌듀비앙 시네마틱 음성 02 사운드
        self.set_skip(state=마무리연출06대기)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='46'):
            return 마무리연출06대기(self.ctx)


class 마무리연출06대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return 마무리연출06(self.ctx)


class 마무리연출06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='47', seconds=5)
        self.set_effect(trigger_ids=[6301]) # 렌듀비앙 시네마틱 음성 02 사운드
        self.set_dialogue(type=2, spawn_id=11001244, script='$52000016_QD__TUTORIAL04__20$', time=4)
        self.set_effect(trigger_ids=[6401], visible=True) # 이슈라 시네마틱 음성 06 사운드
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='47'):
            return 마무리연출07대기(self.ctx)


class 마무리연출07대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return 마무리연출07(self.ctx)


class 마무리연출07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='48', seconds=5)
        self.set_effect(trigger_ids=[6401]) # 이슈라 시네마틱 음성 06 사운드
        self.set_dialogue(type=2, spawn_id=11001230, script='$52000016_QD__TUTORIAL04__21$', time=4)
        self.set_effect(trigger_ids=[6302], visible=True) # 렌듀비앙 시네마틱 음성 03 사운드
        self.set_skip(state=마무리연출08대기)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='48'):
            return 마무리연출08대기(self.ctx)


class 마무리연출08대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return 마무리연출08(self.ctx)


class 마무리연출08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
        self.move_npc(spawn_id=401, patrol_name='MS2PatrolData_4001')
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_1005')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9030, spawn_ids=[401]):
            return 마무리연출09(self.ctx)


class 마무리연출09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='49', seconds=5)
        self.destroy_monster(spawn_ids=[102,401])
        self.set_effect(trigger_ids=[6302]) # 렌듀비앙 시네마틱 음성 03 사운드
        self.set_dialogue(type=2, spawn_id=11001244, script='$52000016_QD__TUTORIAL04__22$', time=3)
        self.set_effect(trigger_ids=[6402], visible=True) # 이슈라 시네마틱 음성 07 사운드
        self.set_skip(state=퇴장준비01대기)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='49'):
            return 퇴장준비01대기(self.ctx)


class 퇴장준비01대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return 퇴장준비01(self.ctx)


class 퇴장준비01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='50', seconds=1)
        self.select_camera(trigger_id=604, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='50'):
            return 퇴장준비02(self.ctx)

    def on_exit(self) -> None:
        self.set_effect(trigger_ids=[6402]) # 이슈라 시네마틱 음성 07 사운드
        self.set_achievement(trigger_id=9040, type='trigger', achieve='complete_tombmission')


class 퇴장준비02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=202, patrol_name='MS2PatrolData_2001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9030, spawn_ids=[202]):
            return 퇴장완료01(self.ctx)


class 퇴장완료01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=10014040, text_id=10014040) # 가이드 : 칼리브 요새로 이동하기
        self.destroy_monster(spawn_ids=[202])

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[9040]):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=10014040)


initial_state = 대기
