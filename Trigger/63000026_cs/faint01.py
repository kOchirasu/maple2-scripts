""" trigger/63000026_cs/faint01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=10000) # BGM
        self.set_effect(trigger_ids=[5000]) # 가이드 서머리 사운드 이펙트
        self.set_effect(trigger_ids=[5100]) # 경로 안내
        self.set_effect(trigger_ids=[5101]) # 경로 안내
        self.set_effect(trigger_ids=[5102]) # 경로 안내
        self.set_effect(trigger_ids=[5103]) # 경로 안내
        self.set_effect(trigger_ids=[5104]) # 경로 안내
        self.set_effect(trigger_ids=[5105]) # 경로 안내
        self.set_effect(trigger_ids=[5106]) # 경로 안내
        self.set_effect(trigger_ids=[5107]) # 경로 안내
        self.set_effect(trigger_ids=[5300]) # Faint
        self.set_effect(trigger_ids=[5400]) # ShadowApp
        self.set_effect(trigger_ids=[6000]) # Voice_Tinchai_00001681
        self.set_effect(trigger_ids=[6001]) # Voice_Tinchai_00001717
        self.set_effect(trigger_ids=[6002]) # Voice_Tinchai_00001682
        self.set_effect(trigger_ids=[6003]) # Voice_Tinchai_00001683
        self.set_agent(trigger_ids=[8000], visible=True)
        self.set_agent(trigger_ids=[8001], visible=True)
        self.set_agent(trigger_ids=[8002], visible=True)
        self.set_agent(trigger_ids=[8003], visible=True)
        self.set_agent(trigger_ids=[8004], visible=True)
        self.set_agent(trigger_ids=[8005], visible=True)
        self.set_agent(trigger_ids=[8006], visible=True)
        self.set_agent(trigger_ids=[8007], visible=True)
        self.set_agent(trigger_ids=[8100])
        self.set_agent(trigger_ids=[8101])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return Enter01(self.ctx)


# 최초 입장
class Enter01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[90000450], quest_states=[1]):
            # 기묘한 조짐 퀘스트 진행중 상태
            return Enter02(self.ctx)


class Enter02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        # 가이드 : 다리를 건너 눈썹달 동굴로 들어가기
        self.show_guide_summary(entity_id=10033010, text_id=10033010)
        self.set_effect(trigger_ids=[5100], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5101], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5102], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5103], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5104], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5105], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5106], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5107], visible=True) # 경로 안내

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9001]):
            return OnTheBridge01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=10033010)
        self.set_effect(trigger_ids=[5100]) # 경로 안내
        self.set_effect(trigger_ids=[5101]) # 경로 안내
        self.set_effect(trigger_ids=[5102]) # 경로 안내
        self.set_effect(trigger_ids=[5103]) # 경로 안내
        self.set_effect(trigger_ids=[5104]) # 경로 안내
        self.set_effect(trigger_ids=[5105]) # 경로 안내
        self.set_effect(trigger_ids=[5106]) # 경로 안내
        self.set_effect(trigger_ids=[5107]) # 경로 안내


class OnTheBridge01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.select_camera(trigger_id=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return OnTheBridge02(self.ctx)


class OnTheBridge02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=63000026, portal_id=10, box_id=9900)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=250):
            return OnTheBridge03(self.ctx)


class OnTheBridge03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_1000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=250):
            return OnTheBridge04(self.ctx)


class OnTheBridge04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.spawn_monster(spawn_ids=[101], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1200):
            return TinChaiComeIn01(self.ctx)


class TinChaiComeIn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=501)
        self.set_sound(trigger_id=10000, enable=True) # BGM

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=700):
            return TinChaiComeIn02(self.ctx)


class TinChaiComeIn02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=101, script='$63000026_CS__FAINT01__5$', time=2)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_101')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=700):
            return TinChaiComeIn03(self.ctx)


class TinChaiComeIn03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_1001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return TinChaiComeIn04(self.ctx)


class TinChaiComeIn04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=502)
        self.set_scene_skip(state=PCTeleport03, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return TinChaiTalk01(self.ctx)


class TinChaiTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6000], visible=True) # Voice_Tinchai_00001681
        self.set_dialogue(type=2, spawn_id=11001708, script='$63000026_CS__FAINT01__0$', time=5) # 틴차이 00001681
        self.set_skip(state=TinChaiTalk02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return TinChaiTalk02(self.ctx)


class TinChaiTalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return TinChaiTalk03(self.ctx)


class TinChaiTalk03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6001], visible=True) # Voice_Tinchai_00001717
        self.set_effect(trigger_ids=[5400], visible=True) # ShadowApp
        self.set_dialogue(type=2, spawn_id=11001708, script='$63000026_CS__FAINT01__1$', time=3) # 틴차이 00001717
        self.spawn_monster(spawn_ids=[900,901,902,903,904,905,910,911,912,913,914,915])
        self.move_npc(spawn_id=900, patrol_name='MS2PatrolData_900')
        self.move_npc(spawn_id=901, patrol_name='MS2PatrolData_901')
        self.move_npc(spawn_id=902, patrol_name='MS2PatrolData_902')
        self.move_npc(spawn_id=903, patrol_name='MS2PatrolData_903')
        self.move_npc(spawn_id=904, patrol_name='MS2PatrolData_904')
        self.move_npc(spawn_id=905, patrol_name='MS2PatrolData_905')
        self.move_npc(spawn_id=910, patrol_name='MS2PatrolData_910')
        self.move_npc(spawn_id=911, patrol_name='MS2PatrolData_911')
        self.move_npc(spawn_id=912, patrol_name='MS2PatrolData_912')
        self.move_npc(spawn_id=913, patrol_name='MS2PatrolData_913')
        self.move_npc(spawn_id=914, patrol_name='MS2PatrolData_914')
        self.move_npc(spawn_id=915, patrol_name='MS2PatrolData_915')
        self.select_camera(trigger_id=600)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return DarkShadowApp01(self.ctx)


# 연출용 그림자 패트롤
class DarkShadowApp01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=601)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return DarkShadowApp02(self.ctx)


class DarkShadowApp02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[102], auto_target=False)
        self.move_user(map_id=63000026, portal_id=20, box_id=9900)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return DarkShadowApp03(self.ctx)


class DarkShadowApp03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=602)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ReadyToBattle01(self.ctx)


class ReadyToBattle01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6002], visible=True) # Voice_Tinchai_00001682
        self.set_dialogue(type=2, spawn_id=11001708, script='$63000026_CS__FAINT01__2$', time=5) # 틴차이 00001682
        self.set_skip(state=ReadyToBattle02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return ReadyToBattle02(self.ctx)


class ReadyToBattle02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.select_camera_path(path_ids=[700,701], return_view=False)
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_102')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return ReadyToBattle03(self.ctx)


class ReadyToBattle03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=63000026, portal_id=30, box_id=9900)
        self.set_effect(trigger_ids=[6001], visible=True) # Voice_Tinchai_00001717
        self.set_dialogue(type=2, spawn_id=11001708, script='$63000026_CS__FAINT01__3$', time=3) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ReadyToBattle05(self.ctx)


class ReadyToBattle05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5300], visible=True) # Faint

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ReadyToBattle06(self.ctx)


class ReadyToBattle06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_pc_emotion_loop(sequence_name='Down_Idle_A', duration=30000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return PCFaint01(self.ctx)


# PC가 털썩 바닥에 쓰러지는 사운드 이펙트
class PCFaint01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=702)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PCFaint02(self.ctx)


class PCFaint02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_103')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PCFaint03(self.ctx)


class PCFaint03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6003], visible=True) # Voice_Tinchai_00001683
        self.set_dialogue(type=2, spawn_id=11001708, script='$63000026_CS__FAINT01__4$', time=5) # 틴차이 00001683
        self.destroy_monster(spawn_ids=[900,901,902,903,904,905,910,911,912,913,914,915])
        self.spawn_monster(spawn_ids=[920,921,922], auto_target=False)
        self.set_skip(state=PCFaint04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return PCFaint04(self.ctx)


class PCFaint04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.destroy_monster(spawn_ids=[102])
        self.spawn_monster(spawn_ids=[103], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return TinChaiGoToFight01(self.ctx)


class TinChaiGoToFight01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=710)
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_104')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return TinChaiGoToFight02(self.ctx)


class TinChaiGoToFight02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return TinChaiGoToFight03(self.ctx)


class TinChaiGoToFight03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.set_agent(trigger_ids=[8000])
        self.set_agent(trigger_ids=[8001])
        self.set_agent(trigger_ids=[8002])
        self.set_agent(trigger_ids=[8003])
        self.set_agent(trigger_ids=[8004])
        self.set_agent(trigger_ids=[8005])
        self.set_agent(trigger_ids=[8006])
        self.set_agent(trigger_ids=[8007])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return PCTeleport01(self.ctx)


class PCTeleport01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[8100], visible=True)
        self.set_agent(trigger_ids=[8101], visible=True)
        self.select_camera_path(path_ids=[720,721])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return PCTeleport02(self.ctx)


class PCTeleport02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return PCTeleport03(self.ctx)


class PCTeleport03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=721, enable=False)
        self.move_user(map_id=63000027, portal_id=1, box_id=9900)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[9900]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
