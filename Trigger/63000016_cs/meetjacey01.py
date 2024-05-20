""" trigger/63000016_cs/meetjacey01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='Guide')
        self.set_portal(portal_id=2, visible=True, minimap_visible=True)
        self.set_mesh(trigger_ids=[3000], visible=True) # MonitorOff
        self.set_mesh(trigger_ids=[3001]) # MonitorOn
        self.set_effect(trigger_ids=[5000]) # 가이드 서머리 사운드 이펙트
        self.set_effect(trigger_ids=[6000]) # RadioInterference

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return WalkIn01(self.ctx)


# 이미 퀘스트 수락한 상태 제이시 가까이로 강제 이동
class MoveToJacey01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=63000016, portal_id=10, box_id=9000)
        self.spawn_monster(spawn_ids=[102], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return MoveToJacey02(self.ctx)


class MoveToJacey02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return JaceyQuest02(self.ctx)


class WalkIn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[90000431], quest_states=[2]):
            # 퀘스트 완료 가능 상태
            return MoveToJacey01(self.ctx)
        if self.wait_tick(wait_tick=2000):
            return WalkIn02(self.ctx)


class WalkIn02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=600)
        self.move_user_path(patrol_name='MS2PatrolData_1000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return WalkIn03(self.ctx)


class WalkIn03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=601)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return MeetJacey01(self.ctx)


class MeetJacey01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.set_dialogue(type=2, spawn_id=11001620, script='$63000016_CS__MEETJACEY01__0$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return MeetJacey02(self.ctx)


class MeetJacey02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=602)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return MeetJacey03(self.ctx)


class MeetJacey03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_1001')
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_101')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return JaceyTalk01(self.ctx)


class JaceyTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Talk_A')
        self.set_dialogue(type=2, spawn_id=11001620, script='$63000016_CS__MEETJACEY01__1$', time=5)
        self.set_skip(state=JaceyTalk02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return JaceyTalk02(self.ctx)


class JaceyTalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return JaceyTalk03(self.ctx)


class JaceyTalk03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_1002')
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_102')
        self.set_dialogue(type=2, spawn_id=11001620, script='$63000016_CS__MEETJACEY01__2$', time=4)
        self.set_skip(state=JaceyTalk04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return JaceyTalk04(self.ctx)


class JaceyTalk04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return JaceyTalk05(self.ctx)


class JaceyTalk05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001620, script='$63000016_CS__MEETJACEY01__3$', time=4)
        self.set_skip(state=JaceyTalk06)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return JaceyTalk06(self.ctx)


class JaceyTalk06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.select_camera(trigger_id=602, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return MinimapGuide01(self.ctx)


# 트리거 To가이드  가이드에서 이동 불가능하게 막기
class MinimapGuide01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 트리거 To가이드 : 탭키 눌러서 미니맵 크게 보기
        self.guide_event(event_id=10021010)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='Guide', name='IsTriggerEvent') == 10021013:
            # 가이드 To 트리거 -: 미니맵 크게 보기 완료
            return MinimapGuide02(self.ctx)


class MinimapGuide02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return JaceyTalk10(self.ctx)


class JaceyTalk10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11001620, script='$63000016_CS__MEETJACEY01__4$', time=4)
        self.set_skip(state=JaceyTalk11)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return JaceyTalk11(self.ctx)


class JaceyTalk11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return JaceyTalk12(self.ctx)


class JaceyTalk12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001620, script='$63000016_CS__MEETJACEY01__5$', time=4)
        self.set_skip(state=JaceyTalk13)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return JaceyTalk13(self.ctx)


class JaceyTalk13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PatrolWithJacey01(self.ctx)


class PatrolWithJacey01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entity_id=10021020, text_id=10021020) # 가이드 : 제이시를 따라 이동하기
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_103')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9100, spawn_ids=[101]):
            return PatrolWithJacey02(self.ctx)


class PatrolWithJacey02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=101, script='$63000016_CS__MEETJACEY01__6$', time=3)
        self.set_dialogue(type=1, spawn_id=101, script='$63000016_CS__MEETJACEY01__7$', time=3, arg5=3)
        self.set_dialogue(type=1, spawn_id=101, script='$63000016_CS__MEETJACEY01__8$', time=3, arg5=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9101, spawn_ids=[101]):
            return PatrolWithJacey03(self.ctx)


class PatrolWithJacey03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=101, script='$63000016_CS__MEETJACEY01__9$', time=3)
        self.set_dialogue(type=1, spawn_id=101, script='$63000016_CS__MEETJACEY01__10$', time=3, arg5=3)
        self.set_dialogue(type=1, spawn_id=101, script='$63000016_CS__MEETJACEY01__11$', time=3, arg5=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9102, spawn_ids=[101]):
            return PatrolWithJacey04(self.ctx)


class PatrolWithJacey04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=101, script='$63000016_CS__MEETJACEY01__12$', time=3)
        self.hide_guide_summary(entity_id=10021020)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return CallNextRoom01(self.ctx)


class CallNextRoom01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=700)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return CallNextRoom02(self.ctx)


class CallNextRoom02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3000], start_delay=100) # MonitorOff
        self.set_mesh(trigger_ids=[3001], visible=True) # MonitorOn
        self.set_effect(trigger_ids=[6000], visible=True) # RadioInterference

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return CallNextRoom03(self.ctx)


class CallNextRoom03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001620, script='$63000016_CS__MEETJACEY01__13$', time=4)
        self.set_skip(state=CallNextRoom04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return CallNextRoom04(self.ctx)


class CallNextRoom04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[102], auto_target=False)
        self.select_camera(trigger_id=700, enable=False)
        self.set_effect(trigger_ids=[6000]) # RadioInterference

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return JaceyQuest00(self.ctx)


# 90000431 퀘스트 수락한 유저를 감지하면
class JaceyQuest00(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entity_id=10021030, text_id=10021030) # 가이드 : 제이시와 대화하기

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9002], quest_ids=[90000431], quest_states=[2]):
            # 퀘스트 진행 중 상태
            return JaceyQuest01(self.ctx)


class JaceyQuest01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=10021030)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return JaceyQuest02(self.ctx)


class JaceyQuest02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11001620, script='$63000016_CS__MEETJACEY01__14$', time=4)
        self.set_skip(state=JaceyQuest03)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return JaceyQuest03(self.ctx)


class JaceyQuest03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return JaceyQuest04(self.ctx)


class JaceyQuest04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001620, script='$63000016_CS__MEETJACEY01__15$', time=4)
        self.destroy_monster(spawn_ids=[102])
        self.spawn_monster(spawn_ids=[103], auto_target=False)
        self.set_skip(state=JaceyQuest05)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return JaceyQuest05(self.ctx)


class JaceyQuest05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return AboutPotion01(self.ctx)


class AboutPotion01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001620, script='$63000016_CS__MEETJACEY01__16$', time=4)
        self.set_skip(state=AboutPotion02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return AboutPotion02(self.ctx)


class AboutPotion02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return AboutPotion03(self.ctx)


class AboutPotion03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001620, script='$63000016_CS__MEETJACEY01__17$', time=4)
        self.set_skip(state=AboutPotion04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return AboutPotion04(self.ctx)


class AboutPotion04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_301')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return JaceyLeve01(self.ctx)

    def on_exit(self) -> None:
        self.guide_event(event_id=10021120) # 트리거 To가이드 : PC 컨트롤 불가


class JaceyLeve01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=103, script='$63000016_CS__MEETJACEY01__18$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return JaceyLeve02(self.ctx)


class JaceyLeve02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.destroy_monster(spawn_ids=[103])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return SendSignalToGuide01(self.ctx)


# 트리거 To가이드
class SendSignalToGuide01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 트리거 To가이드 : 약초 퀵슬롯에 장착하기
        self.guide_event(event_id=10021050)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return PortalOpen01(self.ctx)


class PortalOpen01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[9002]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
