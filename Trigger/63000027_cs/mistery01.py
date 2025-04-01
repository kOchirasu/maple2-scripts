""" trigger/63000027_cs/mistery01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000]) # 가이드 서머리 사운드 이펙트
        self.set_effect(trigger_ids=[5200]) # VibrateLong
        self.set_effect(trigger_ids=[5300]) # Sound_SpaceDestroy
        self.set_effect(trigger_ids=[5400]) # Voice_Vision_00001725
        self.set_effect(trigger_ids=[5401]) # Voice_Vision_00001741
        self.set_effect(trigger_ids=[5402]) # Voice_Vision_00001872
        self.set_effect(trigger_ids=[5500]) # Sound_VisionBuff
        self.set_mesh(trigger_ids=[3100]) # barrier
        self.set_mesh(trigger_ids=[3101]) # barrier
        self.set_mesh(trigger_ids=[3102]) # barrier
        self.set_mesh(trigger_ids=[3103]) # barrier
        self.set_user_value(key='CollapseEnd', value=0)
        self.set_user_value(key='ZoomIn', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return Enter01(self.ctx)


# 최초 입장
class Enter01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[90000451], quest_states=[1]):
            # 별, 수정, 그리고 퀘스트 수락한 상태
            return QuestOnGoing01(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[90000450], quest_states=[3]):
            # 기묘한 조짐 퀘스트 완료 상태
            return QuestOnGoing11(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[90000450], quest_states=[2]):
            # 기묘한 조짐 퀘스트 완료 가능 상태
            return Delay01(self.ctx)
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


# 별, 수정, 그리고 퀘스트 수락한 상태
class QuestOnGoing01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[102], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return TimeToLeave01(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


# 기묘한 조짐 퀘스트 완료 상태
class QuestOnGoing11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[102], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return SecondQuestStart01(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class Delay01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=500)
        self.set_scene_skip(state=VisionApp02, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return LookAround01(self.ctx)


class LookAround01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return LookAround02(self.ctx)


class LookAround02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=501)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return LookAround03(self.ctx)


class LookAround03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_1000')
        self.set_dialogue(type=1, script='$63000027_CS__MISTERY01__0$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return LookAround04(self.ctx)


class LookAround04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=502)
        self.set_pc_emotion_sequence(sequence_names=['Bore_C'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return VisionApp01(self.ctx)


class VisionApp01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=600)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return VisionApp02(self.ctx)


class VisionApp02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_101')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return VisionTalk01(self.ctx)


class VisionTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5400], visible=True) # Voice_Vision_00001725
        self.set_dialogue(type=2, spawn_id=11001560, script='$63000027_CS__MISTERY01__1$', time=5) # Voice 00001725
        self.set_skip(state=VisionTalk04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return VisionTalk02(self.ctx)


class VisionTalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return VisionTalk03(self.ctx)


class VisionTalk03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001560, script='$63000027_CS__MISTERY01__2$', time=5)
        self.set_skip(state=VisionTalk04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return VisionTalk04(self.ctx)


class VisionTalk04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[102], auto_target=False)
        self.select_camera(trigger_id=601, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return VisionTalk05(self.ctx)


class VisionTalk05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return FirstQuestEnd01(self.ctx)


class FirstQuestEnd01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entity_id=10034010, text_id=10034010) # 가이드 : 비전을 향해 이동하기

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9100]):
            return FirstQuestEnd02(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=10034010)


class FirstQuestEnd02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        # 가이드 : [[icon:questcomplete]] 비전과 대화하기
        self.show_guide_summary(entity_id=10034020, text_id=10034020)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000450], quest_states=[3]):
            # 기묘한 조짐 퀘스트 완료 상태
            return SecondQuestStart01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=10034020)


class SecondQuestStart01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        # 가이드 : [[icon:questaccept]] 비전과 대화하기
        self.show_guide_summary(entity_id=10034030, text_id=10034030)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000451], quest_states=[1]):
            # 별, 수정, 그리고 퀘스트 수락한 상태
            return TimeToLeave01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=10034030)


class TimeToLeave01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.select_camera(trigger_id=700)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=250):
            return TimeToLeave02(self.ctx)


class TimeToLeave02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[102])
        self.spawn_monster(spawn_ids=[103], auto_target=False)
        self.move_user(map_id=63000027, portal_id=10, box_id=9900)
        self.set_scene_skip(state=VisionSayGoodbye04, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=250):
            return TimeToLeave03(self.ctx)


class TimeToLeave03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=701)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return PCGetEffect01(self.ctx)


class PCGetEffect01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[9900], skill_id=70000097, level=1) # 신비로운 힘
        self.set_effect(trigger_ids=[5500], visible=True) # Sound_VisionBuff

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return VisionSayGoodbye01(self.ctx)


class VisionSayGoodbye01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5402], visible=True) # Voice_Vision_00001872
        self.set_dialogue(type=1, spawn_id=103, script='$63000027_CS__MISTERY01__3$', time=4) # Voice 00001872

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return VisionSayGoodbye02(self.ctx)


class VisionSayGoodbye02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5401], visible=True) # Voice_Vision_00001741
        self.set_dialogue(type=1, spawn_id=103, script='$63000027_CS__MISTERY01__4$', time=4) # Voice 00001741
        self.set_dialogue(type=1, spawn_id=103, script='$63000027_CS__MISTERY01__5$', time=3, arg5=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return VisionSayGoodbye03(self.ctx)


class VisionSayGoodbye03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_102')
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return VisionSayGoodbye04(self.ctx)


class VisionSayGoodbye04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[103])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Collapse01(self.ctx)


class Collapse01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5200], visible=True) # VibrateLong
        self.select_camera(trigger_id=710)
        self.set_mesh(trigger_ids=[3100], visible=True) # barrier
        self.set_mesh(trigger_ids=[3101], visible=True) # barrier
        self.set_mesh(trigger_ids=[3102], visible=True) # barrier
        self.set_mesh(trigger_ids=[3103], visible=True) # barrier
        self.set_user_value(trigger_id=2, key='CollapseStart', value=1)
        self.set_effect(trigger_ids=[5300], visible=True) # Sound_SpaceDestroy

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ZoomIn') == 1:
            return Collapse02(self.ctx)


class Collapse02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=711)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CollapseEnd') == 1:
            return PCFainted01(self.ctx)


class PCFainted01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_sequence(sequence_names=['Down2_A','Down_Idle_A'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2667):
            return PCTeleport01(self.ctx)


class PCTeleport01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_loop(sequence_name='Down_Idle_A', duration=10000.0)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return PCTeleport02(self.ctx)


class PCTeleport02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=63000028, portal_id=1, box_id=9900)
        self.select_camera(trigger_id=711, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[9900]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = Wait
