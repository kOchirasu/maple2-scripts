""" trigger/63000015_cs/intro01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='Guide')
        self.set_sound(trigger_id=10000)
        self.set_portal(portal_id=1)
        self.set_mesh(trigger_ids=[3001,3002,3003,3004], visible=True) # barrier
        self.set_effect(trigger_ids=[5100]) # 목표지점 바닥
        self.set_effect(trigger_ids=[5101]) # 목표지점 화살표
        self.set_effect(trigger_ids=[5000]) # 가이드 서머리 사운드 이펙트
        self.set_effect(trigger_ids=[5001]) # 목료 완료 사운드 이펙트
        self.set_effect(trigger_ids=[5002]) # 화살표 안내 사운드 이펙트
        self.set_effect(trigger_ids=[5200]) # 경로 안내
        self.set_effect(trigger_ids=[5201]) # 경로 안내
        self.set_effect(trigger_ids=[5202]) # 경로 안내
        self.set_effect(trigger_ids=[5203]) # 경로 안내
        self.set_effect(trigger_ids=[5204]) # 경로 안내
        self.set_effect(trigger_ids=[5205]) # 경로 안내
        self.set_effect(trigger_ids=[5206]) # 경로 안내
        self.set_effect(trigger_ids=[5207]) # 경로 안내
        self.set_effect(trigger_ids=[6000]) # VoiceGangster
        self.set_effect(trigger_ids=[8000]) # WeiHong 00001390
        self.set_effect(trigger_ids=[8001]) # WeiHong 00001391
        self.set_effect(trigger_ids=[8002]) # WeiHong 00001392
        self.set_effect(trigger_ids=[8003]) # WeiHong 00001393
        self.set_effect(trigger_ids=[8004]) # WeiHong 00001394
        self.set_effect(trigger_ids=[8005]) # WeiHong 00000480
        self.spawn_monster(spawn_ids=[101,201,202,203,204,205,206], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return PlayOpeningMovie01(self.ctx)


# 퀘스트 진행 중 상태, 완료 가능 상태
class StandAside10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=10000, enable=True)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_mesh(trigger_ids=[3001,3002,3003,3004]) # barrier
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[102], auto_target=False)
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_201')
        self.move_npc(spawn_id=202, patrol_name='MS2PatrolData_202')
        self.move_npc(spawn_id=204, patrol_name='MS2PatrolData_204')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return StandAside11(self.ctx)


class StandAside11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=203, patrol_name='MS2PatrolData_203')
        self.move_npc(spawn_id=205, patrol_name='MS2PatrolData_205')
        self.move_npc(spawn_id=206, patrol_name='MS2PatrolData_206')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=400):
            return WeiHongQuest03(self.ctx)


# 퀘스트 진행 완료 상태
class StandAside20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=10000, enable=True)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_mesh(trigger_ids=[3001,3002,3003,3004]) # barrier
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[102], auto_target=False)
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_201')
        self.move_npc(spawn_id=202, patrol_name='MS2PatrolData_202')
        self.move_npc(spawn_id=204, patrol_name='MS2PatrolData_204')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return StandAside21(self.ctx)


class StandAside21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=203, patrol_name='MS2PatrolData_203')
        self.move_npc(spawn_id=205, patrol_name='MS2PatrolData_205')
        self.move_npc(spawn_id=206, patrol_name='MS2PatrolData_206')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=400):
            return GuideNextMap01(self.ctx)


# 최초 입장
class PlayOpeningMovie01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9100], quest_ids=[90000430], quest_states=[2]):
            # 퀘스트 완료 가능 상태
            return StandAside10(self.ctx)
        if self.quest_user_detected(box_ids=[9100], quest_ids=[90000430], quest_states=[3]):
            # 퀘스트 완료 상태
            return StandAside20(self.ctx)
        if self.wait_tick(wait_tick=2000):
            return PlayOpeningMovie02(self.ctx)


class PlayOpeningMovie02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(file_name='common\\Common_Opening.usm', movie_id=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 2:
            return PlayMovie01(self.ctx)
        if self.wait_tick(wait_tick=190000):
            return PlayMovie01(self.ctx)


class PlayMovie01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return PlayMovie02(self.ctx)


class PlayMovie02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(file_name='Cut_Blackstar_Crash.swf', movie_id=1) # 임시

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return WeiHongTalk01(self.ctx)
        if self.wait_tick(wait_tick=66000):
            return WeiHongTalk01(self.ctx)


class WeiHongTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=10000, enable=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=600)
        self.set_effect(trigger_ids=[6000], visible=True) # VoiceGangster

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return WeiHongTalk02(self.ctx)

    def on_exit(self) -> None:
        self.set_effect(trigger_ids=[6000]) # VoiceGangster


class WeiHongTalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=601)
        self.set_dialogue(type=2, spawn_id=11000251, script='$63000015_CS__INTRO01__0$', time=6) # Voice 00001390
        self.set_effect(trigger_ids=[8000], visible=True) # WeiHong 00001390
        self.set_skip(state=WeiHongTalk03)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return WeiHongTalk03(self.ctx)


class WeiHongTalk03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_effect(trigger_ids=[8000]) # WeiHong 00001390

    def on_tick(self) -> trigger_api.Trigger:
        return WeiHongTalk04(self.ctx)


class WeiHongTalk04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000251, script='$63000015_CS__INTRO01__1$', time=6) # Voice 00001391
        self.set_effect(trigger_ids=[8001], visible=True) # WeiHong 00001391
        self.set_skip(state=WeiHongTalk05)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return WeiHongTalk05(self.ctx)


class WeiHongTalk05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_effect(trigger_ids=[8001]) # WeiHong 00001391

    def on_tick(self) -> trigger_api.Trigger:
        return WeiHongTalk06(self.ctx)


class WeiHongTalk06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000251, script='$63000015_CS__INTRO01__2$', time=5) # Voice 00001392
        self.set_effect(trigger_ids=[8002], visible=True) # WeiHong 00001392
        self.set_skip(state=WeiHongTalk07)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return WeiHongTalk07(self.ctx)


class WeiHongTalk07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_effect(trigger_ids=[8002]) # WeiHong 00001392
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=601, enable=False)
        self.set_mesh(trigger_ids=[3001,3002,3003,3004]) # barrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return StandAside01(self.ctx)


class StandAside01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_201')
        self.move_npc(spawn_id=202, patrol_name='MS2PatrolData_202')
        self.move_npc(spawn_id=204, patrol_name='MS2PatrolData_204')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return StandAside02(self.ctx)


class StandAside02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=203, patrol_name='MS2PatrolData_203')
        self.move_npc(spawn_id=205, patrol_name='MS2PatrolData_205')
        self.move_npc(spawn_id=206, patrol_name='MS2PatrolData_206')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=400):
            return StandAside03(self.ctx)


class StandAside03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return KeytypeSelect01(self.ctx)


class KeytypeSelect01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.guide_event(event_id=10020005)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='Guide', name='IsTriggerEvent') == 10020009:
            return MeetWeiHong01(self.ctx)


class MeetWeiHong01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_effect(trigger_ids=[5002], visible=True) # 화살표 안내 사운드 이펙트
        self.set_effect(trigger_ids=[5100], visible=True) # 목표지점 바닥
        self.set_effect(trigger_ids=[5101], visible=True) # 목표지점 화살표
        # 가이드 : 방향키를 이용해 화살표가 가리키는 곳으로 이동하기
        self.show_guide_summary(entity_id=10020010, text_id=10020010)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9001]):
            return MeetWeiHong02(self.ctx)


class MeetWeiHong02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001], visible=True) # 미션 완료 사운드 이펙트
        self.set_effect(trigger_ids=[5000]) # 가이드 서머리 사운드 이펙트
        self.set_effect(trigger_ids=[5002]) # 화살표 안내 사운드 이펙트
        self.set_effect(trigger_ids=[5100]) # 목표지점 바닥
        self.set_effect(trigger_ids=[5101]) # 목표지점 화살표
        self.hide_guide_summary(entity_id=10020010)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return WeiHongTalk10(self.ctx)


class WeiHongTalk10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=602)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return WeiHongTalk11(self.ctx)


class WeiHongTalk11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000251, script='$63000015_CS__INTRO01__3$', time=5) # Voice 00000480
        self.set_effect(trigger_ids=[8005], visible=True) # WeiHong 00000480
        self.set_skip(state=WeiHongTalk12)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return WeiHongTalk12(self.ctx)


class WeiHongTalk12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_effect(trigger_ids=[8005]) # WeiHong 00000480
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        return WeiHongTalk13(self.ctx)


class WeiHongTalk13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000251, script='$63000015_CS__INTRO01__4$', time=5) # Voice 00001393
        self.set_effect(trigger_ids=[8003], visible=True) # WeiHong 00001393
        self.set_skip(state=WeiHongTalk14)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return WeiHongTalk14(self.ctx)


class WeiHongTalk14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_effect(trigger_ids=[8003]) # WeiHong 00001393
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        return MafiaTalk10(self.ctx)


class MafiaTalk10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6000], visible=True) # VoiceGangster
        self.set_dialogue(type=1, spawn_id=201, script='$63000015_CS__INTRO01__5$', time=3)
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Talk_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return MafiaTalk11(self.ctx)


class MafiaTalk11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Idle_A')
        self.set_dialogue(type=1, spawn_id=202, script='$63000015_CS__INTRO01__6$', time=3)
        self.set_npc_emotion_sequence(spawn_id=202, sequence_name='Talk_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return MafiaTalk12(self.ctx)


class MafiaTalk12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=202, sequence_name='Idle_A')
        self.set_dialogue(type=1, spawn_id=206, script='$63000015_CS__INTRO01__7$', time=3)
        self.set_npc_emotion_sequence(spawn_id=206, sequence_name='Talk_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return WeiHongTalk20(self.ctx)

    def on_exit(self) -> None:
        self.set_effect(trigger_ids=[6000]) # VoiceGangster


class WeiHongTalk20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=206, sequence_name='Idle_A')
        self.set_dialogue(type=2, spawn_id=11000251, script='$63000015_CS__INTRO01__8$', time=6) # Voice 00001394
        self.set_effect(trigger_ids=[8004], visible=True) # WeiHong 00001394
        self.set_skip(state=WeiHongQuest01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return WeiHongQuest01(self.ctx)


class WeiHongQuest01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_effect(trigger_ids=[8004]) # WeiHong 00001394
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[102], auto_target=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=602, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return WeiHongQuest02(self.ctx)


class WeiHongQuest02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entity_id=10020020, text_id=10020020) # 가이드 : 스페이스키로 대화하기

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9100], quest_ids=[90000430], quest_states=[2]):
            # 퀘스트 진행 중 상태
            return WeiHongQuest03(self.ctx)


class WeiHongQuest03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=10020020)
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entity_id=10020021, text_id=10020021) # 가이드 : 웨이 홍과 대화하기

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9100], quest_ids=[90000430], quest_states=[3]):
            # 퀘스트 완료 상태
            return GuideNextMap01(self.ctx)


class GuideNextMap01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=10020021)
        self.set_portal(portal_id=1, visible=True, minimap_visible=True)
        self.set_effect(trigger_ids=[5200], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5201], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5202], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5203], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5204], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5205], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5206], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5207], visible=True) # 경로 안내
        # 가이드 : 방향키를 이용해 화살표가 가리키는 곳으로 이동하기
        self.show_guide_summary(entity_id=10020012, text_id=10020012)
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9002]):
            return GuideNextMap02(self.ctx)


class GuideNextMap02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=10020012)
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)
        self.show_guide_summary(entity_id=10020011, text_id=10020011) # 가이드 : 포털 위치에서 스페이스 키 누르기
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[9100]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=10020011)
        self.set_effect(trigger_ids=[5200]) # 경로 안내
        self.set_effect(trigger_ids=[5201]) # 경로 안내
        self.set_effect(trigger_ids=[5202]) # 경로 안내
        self.set_effect(trigger_ids=[5203]) # 경로 안내
        self.set_effect(trigger_ids=[5204]) # 경로 안내
        self.set_effect(trigger_ids=[5205]) # 경로 안내
        self.set_effect(trigger_ids=[5206]) # 경로 안내
        self.set_effect(trigger_ids=[5207]) # 경로 안내


initial_state = Wait
