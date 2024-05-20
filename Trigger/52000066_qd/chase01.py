""" trigger/52000066_qd/chase01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[1000]) # LadderEnterance
        self.set_ladder(trigger_ids=[1001]) # LadderEnterance
        self.set_ladder(trigger_ids=[1002]) # LadderEnterance
        self.set_ladder(trigger_ids=[1003]) # LadderEnterance
        self.set_ladder(trigger_ids=[1004]) # LadderEnterance
        self.set_ladder(trigger_ids=[1005]) # LadderEnterance
        self.set_actor(trigger_id=4000, visible=True, initial_sequence='Closed') # TrapLever
        self.set_mesh(trigger_ids=[2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029], visible=True, fade=3.0) # TrapMesh
        self.set_effect(trigger_ids=[5001]) # DownArrow
        self.set_breakable(trigger_ids=[4100]) # Move_Agent
        self.set_breakable(trigger_ids=[4200]) # Move_Train
        self.set_visible_breakable_object(trigger_ids=[4100]) # Move_Agent
        self.set_visible_breakable_object(trigger_ids=[4200]) # Move_Train
        self.set_portal(portal_id=2, visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return LodingDelay01(self.ctx)


class LodingDelay01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return PCMonologue01(self.ctx)


class PCMonologue01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_1002')
        self.set_dialogue(type=1, script='$52000066_QD__CHASE01__0$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return LodingDelay02(self.ctx)


class LodingDelay02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=600)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FirstCameraGuide01(self.ctx)


class FirstCameraGuide01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_101')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return FirstCameraGuide02(self.ctx)


class FirstCameraGuide02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=600, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FirstPhaseChase01(self.ctx)


class FirstPhaseChase01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101])
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='$52000066_QD__CHASE01__1$', arg3='3000', arg4='0')
        self.set_ladder(trigger_ids=[1000], visible=True, enable=True) # LadderEnterance
        self.set_ladder(trigger_ids=[1001], visible=True, enable=True) # LadderEnterance
        self.set_ladder(trigger_ids=[1002], visible=True, enable=True) # LadderEnterance
        self.set_ladder(trigger_ids=[1003], visible=True, enable=True) # LadderEnterance
        self.set_ladder(trigger_ids=[1004], visible=True, enable=True) # LadderEnterance
        self.set_ladder(trigger_ids=[1005], visible=True, enable=True) # LadderEnterance

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9200]):
            # 트랩 레버 주변
            return SecondCameraGuide01(self.ctx)


class SecondCameraGuide01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=601)
        self.spawn_monster(spawn_ids=[102], auto_target=False)
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_102')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return SecondCameraGuide02(self.ctx)


class SecondCameraGuide02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000066, portal_id=40)
        self.set_actor(trigger_id=4000, visible=True, initial_sequence='Opened') # TrapLever
        self.set_mesh(trigger_ids=[2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029], start_delay=500, interval=50, fade=1.0) # TrapMesh

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return SecondCameraGuide03(self.ctx)


class SecondCameraGuide03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=601, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return SecondPhaseChase01(self.ctx)


class SecondPhaseChase01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_1001')
        self.set_dialogue(type=1, script='$52000066_QD__CHASE01__2$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return SecondPhaseChase02(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class SecondPhaseChase02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[102])
        self.set_user_value(trigger_id=2, key='TrapLeverOn', value=1)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        # 가이드 : 함정을 뛰어 넘거나 레버를 당겨 보세요.
        self.show_guide_summary(entity_id=25200661, text_id=25200661, duration=6000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9300]):
            # 엘베 주변
            return ThirdPhaseChase01(self.ctx)


class ThirdPhaseChase01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=25200662, text_id=25200662) # 가이드 : 발판을 타고 위로 올라가세요.

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9400,9401,9402,9403,9404,9405,9406]):
            # 엘베 위 도착
            return ThirdCameraGuide01(self.ctx)


# 범인이 수레타고 도망가는 연출
class ThirdCameraGuide01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2, key='TrapLeverOn', value=2)
        self.hide_guide_summary(entity_id=25200662)
        self.set_breakable(trigger_ids=[4100], enable=True) # Move_Agent
        self.set_breakable(trigger_ids=[4200], enable=True) # Move_Train
        self.set_visible_breakable_object(trigger_ids=[4100], visible=True) # Move_Agent
        self.set_visible_breakable_object(trigger_ids=[4200], visible=True) # Move_Train

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return ThirdCameraGuide02(self.ctx)


class ThirdCameraGuide02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=602)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ThirdCameraGuide03(self.ctx)

    def on_exit(self) -> None:
        self.move_user(map_id=52000066, portal_id=30)


class ThirdCameraGuide03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=604)
        self.move_user_path(patrol_name='MS2PatrolData_1000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return PCMonologue10(self.ctx)


class PCMonologue10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000066_QD__CHASE01__3$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return FourthTrainMove01(self.ctx)

    def on_exit(self) -> None:
        self.select_camera(trigger_id=604, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class FourthTrainMove01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_breakable(trigger_ids=[4100]) # Move_Agent
        self.set_breakable(trigger_ids=[4200]) # Move_Train
        self.set_visible_breakable_object(trigger_ids=[4100]) # Move_Agent
        self.set_visible_breakable_object(trigger_ids=[4200]) # Move_Train
        self.set_user_value(trigger_id=3, key='TrainMove', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9500,9501,9502]):
            # 레일 끝 도착
            return AgentEscape01(self.ctx)


class AgentEscape01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[103], auto_target=False)
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_103')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return AgentEscape02(self.ctx)


class AgentEscape02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=603)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9600, spawn_ids=[103]):
            return AgentEscape03(self.ctx)


class AgentEscape03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_item(spawn_ids=[300], arg5=6000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return AgentEscape04(self.ctx)


class AgentEscape04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[103])
        self.select_camera(trigger_id=603, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return PCMonologue20(self.ctx)


class PCMonologue20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000066_QD__CHASE01__4$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return QuestEndCheck01(self.ctx)


class QuestEndCheck01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[10001028], quest_states=[2]):
            # 초보자 넬프가남긴것 퀘스트 완료가능
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2, visible=True, enable=True)


initial_state = Wait
