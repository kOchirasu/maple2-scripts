""" trigger/63000024_cs/wakeup01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='Guide')
        self.set_portal(portal_id=1)
        self.set_effect(trigger_ids=[5000]) # 가이드 서머리 사운드 이펙트
        self.set_effect(trigger_ids=[5001]) # 화살표 안내 사운드 이펙트
        self.set_effect(trigger_ids=[5002]) # 미션 완료 사운드 이펙트
        self.set_effect(trigger_ids=[5100]) # 목표 바닥 지점01 NPC
        self.set_effect(trigger_ids=[5102]) # 목표 바닥 지점03 포탈
        self.set_effect(trigger_ids=[5200]) # 화살표01 NPC
        self.set_effect(trigger_ids=[5300]) # 경로 안내
        self.set_effect(trigger_ids=[5301]) # 경로 안내
        self.set_effect(trigger_ids=[5302]) # 경로 안내
        self.set_effect(trigger_ids=[5303]) # 경로 안내
        self.set_effect(trigger_ids=[5304]) # 경로 안내
        self.set_effect(trigger_ids=[5500]) # 경로 안내
        self.set_effect(trigger_ids=[5501]) # 경로 안내
        self.set_effect(trigger_ids=[5502]) # 경로 안내
        self.set_effect(trigger_ids=[5503]) # 경로 안내
        self.set_effect(trigger_ids=[5504]) # 경로 안내
        self.set_effect(trigger_ids=[5505]) # 경로 안내
        self.set_effect(trigger_ids=[5506]) # 경로 안내
        self.set_effect(trigger_ids=[6000]) # Voice_Tinchai_00001674
        self.set_effect(trigger_ids=[6001]) # Voice_Tinchai_00001714
        self.set_effect(trigger_ids=[6002]) # Voice_Tinchai_00001675
        self.spawn_monster(spawn_ids=[101], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return PlayMovie01(self.ctx)


class PlayMovie01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000444], quest_states=[1]):
            # 두 번째 퀘스트 수락한 상태
            return QuestOnGoing04(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000443], quest_states=[3]):
            # 첫 번째 퀘스트 완료 상태
            return QuestOnGoing03(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000443], quest_states=[2]):
            # 첫 번째 퀘스트 완료 가능 상태
            return QuestOnGoing02(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000443], quest_states=[1]):
            # 첫 번째 퀘스트 수락한 상태
            return QuestOnGoing01(self.ctx)
        if self.wait_tick(wait_tick=2000):
            return LodingDelay01(self.ctx)


# 첫 번째 퀘스트 수락한 상태
class QuestOnGoing01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=63000024, portal_id=10, box_id=9900)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[102], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return None # Missing State: MoveToGetWeapon01


# 첫 번째 퀘스트 완료 가능 상태
class QuestOnGoing02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=63000024, portal_id=10, box_id=9900)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[102], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return QuestStart02(self.ctx)


# 첫 번째 퀘스트 완료 상태
class QuestOnGoing03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=63000024, portal_id=10, box_id=9900)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[102], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return QuestStart03(self.ctx)


# 두 번째 퀘스트 수락한 상태
class QuestOnGoing04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=63000024, portal_id=10, box_id=9900)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[103], auto_target=False)
        self.set_portal(portal_id=1, visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return TimeToLeave01(self.ctx)


# 최초 입장
class LodingDelay01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=500)
        self.set_scene_skip(state=TinChaiTalk04_CSkip, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PCDownIdle01(self.ctx)


class PCDownIdle01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_loop(sequence_name='Down_Idle_D', duration=9000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PCDownIdle02(self.ctx)


class PCDownIdle02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return LookAround01(self.ctx)


class LookAround01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[501,502], return_view=False)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_101')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return LookAround02(self.ctx)


class LookAround02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_loop(sequence_name='Sit_Ground_Idle_A', duration=18000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return LookAround03(self.ctx)


class LookAround03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return LookAround04(self.ctx)


class LookAround04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=510)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_105')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return LookAround05(self.ctx)


class LookAround05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return LookAround06(self.ctx)


class LookAround06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=511)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return LookAround07(self.ctx)


class LookAround07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=600)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_102')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return TinChaiTalk01(self.ctx)


class TinChaiTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6000], visible=True) # Voice_Tinchai_00001674
        self.set_dialogue(type=2, spawn_id=11001708, script='$63000024_CS__WAKEUP01__0$', time=7) # Voice 00001674
        self.set_skip(state=TinChaiTalk02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return TinChaiTalk02(self.ctx)


class TinChaiTalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return TinChaiTalk03(self.ctx)


class TinChaiTalk03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6001], visible=True) # Voice_Tinchai_00001714
        self.set_dialogue(type=2, spawn_id=11001708, script='$63000024_CS__WAKEUP01__1$', time=5) # Voice 00001714
        self.set_skip(state=TinChaiTalk04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return TinChaiTalk04(self.ctx)


class TinChaiTalk04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.move_user(map_id=63000024, portal_id=10, box_id=9900)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=600, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 키타입설정안내01(self.ctx)


class TinChaiTalk04_CSkip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_102')
        self.move_user(map_id=63000024, portal_id=10, box_id=9900)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=600, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 키타입설정안내01(self.ctx)


class 키타입설정안내01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.guide_event(event_id=10030005) # 트리거 To가이드 : 키타입설정

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='Guide', name='IsTriggerEvent') == 10030009:
            return MeetTinChai01(self.ctx)


class MeetTinChai01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_effect(trigger_ids=[5001], visible=True) # 화살표 안내 사운드 이펙트
        self.set_effect(trigger_ids=[5100], visible=True) # 목표 바닥 지점01 NPC
        self.set_effect(trigger_ids=[5200], visible=True) # 화살표01 NPC
        self.set_effect(trigger_ids=[5300], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5301], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5302], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5303], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5304], visible=True) # 경로 안내
        # 가이드 : 방향키를 이용해 화살표가 가리키는 곳으로 이동하기
        self.show_guide_summary(entity_id=10030010, text_id=10030010)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9001]):
            return MeetTinChai02(self.ctx)


class MeetTinChai02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000]) # 가이드 서머리 사운드 이펙트
        self.set_effect(trigger_ids=[5001]) # 화살표 안내 사운드 이펙트
        self.set_effect(trigger_ids=[5002], visible=True) # 미션 완료 사운드 이펙트
        self.set_effect(trigger_ids=[5100]) # 목표 바닥 지점01 NPC
        self.set_effect(trigger_ids=[5200]) # 화살표01 NPC
        self.set_effect(trigger_ids=[5300]) # 경로 안내
        self.set_effect(trigger_ids=[5301]) # 경로 안내
        self.set_effect(trigger_ids=[5302]) # 경로 안내
        self.set_effect(trigger_ids=[5303]) # 경로 안내
        self.set_effect(trigger_ids=[5304]) # 경로 안내
        self.hide_guide_summary(entity_id=10030010)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return TinChaiTalk10(self.ctx)


class TinChaiTalk10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return TinChaiTalk11(self.ctx)


class TinChaiTalk11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6002], visible=True) # Voice_Tinchai_00001675
        self.set_dialogue(type=2, spawn_id=11001708, script='$63000024_CS__WAKEUP01__2$', time=6) # Voice 00001675
        self.set_skip(state=TinChaiTalk14)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return TinChaiTalk12(self.ctx)


class TinChaiTalk12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return TinChaiTalk13(self.ctx)


class TinChaiTalk13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001708, script='$63000024_CS__WAKEUP01__3$', time=5)
        self.set_skip(state=TinChaiTalk14)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return TinChaiTalk14(self.ctx)


class TinChaiTalk14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[102], auto_target=False)
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        # 가이드 : 틴차이에게 다가가 스페이스키로 대화하기
        self.show_guide_summary(entity_id=10030020, text_id=10030020)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000443], quest_states=[1]):
            # 90000443 신비로운 보옥 수락한 상태
            return QuestStart01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=10030020)


# 오브젝트 반응, 아이템 줍기, 무기 장착, 일반 공격 가이드
class QuestStart01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000443], quest_states=[2]):
            # 90000443 신비로운 보옥 완료 가능
            return QuestStart02(self.ctx)


class QuestStart02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000443], quest_states=[3]):
            # 90000443 신비로운 보옥 완료
            return QuestStart03(self.ctx)


# 약초 장착 가이드
class QuestStart03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000444], quest_states=[1]):
            # 90000444 가이던스의 대제자 수락
            return QuestStart04(self.ctx)


class QuestStart04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=1, visible=True)
        self.destroy_monster(spawn_ids=[102])
        self.spawn_monster(spawn_ids=[103], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return TimeToLeave01(self.ctx)


class TimeToLeave01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_103')
        self.set_dialogue(type=1, spawn_id=103, script='$63000024_CS__WAKEUP01__4$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return GuideNextMap01(self.ctx)


class GuideNextMap01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        # 가이드 : 방향키를 이용해 화살표가 가리키는 곳으로 이동하기
        self.show_guide_summary(entity_id=10030010, text_id=10030010)
        self.set_effect(trigger_ids=[5001], visible=True) # 화살표 안내 사운드 이펙트
        self.set_effect(trigger_ids=[5102], visible=True) # 목표 바닥 지점03 포탈
        self.set_effect(trigger_ids=[5500], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5501], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5502], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5503], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5504], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5505], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5506], visible=True) # 경로 안내

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9003]):
            return GuideNextMap02(self.ctx)


class GuideNextMap02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_104')
        self.hide_guide_summary(entity_id=10030010)
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)
        self.set_effect(trigger_ids=[5002], visible=True) # 미션 완료 사운드 이펙트
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entity_id=1060, text_id=1060) # 가이드 : 포털 위치에서 스페이스 키 누르기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return GuideNextMap03(self.ctx)


class GuideNextMap03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[103])

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[9900]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=1060)


initial_state = Wait
