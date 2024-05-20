""" trigger/63000020_cs/battle01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000]) # 가이드 서머리 사운드 이펙트
        self.set_effect(trigger_ids=[5001]) # 미션 완료 사운드 이펙트
        self.spawn_monster(spawn_ids=[101,201,301,401,501], auto_target=False)
        self.set_agent(trigger_ids=[8000], visible=True)
        self.set_agent(trigger_ids=[8001], visible=True)
        self.set_agent(trigger_ids=[8002], visible=True)
        self.set_agent(trigger_ids=[8003], visible=True)
        self.set_agent(trigger_ids=[8004], visible=True)
        self.set_agent(trigger_ids=[8005], visible=True)
        self.set_agent(trigger_ids=[8006], visible=True)
        self.set_agent(trigger_ids=[8007], visible=True)
        self.set_agent(trigger_ids=[8008], visible=True)
        self.set_skill(trigger_ids=[7000]) # PCKnockBack
        self.set_effect(trigger_ids=[7001]) # VibrateDizzy
        self.set_effect(trigger_ids=[6000]) # RingBellStart
        self.set_effect(trigger_ids=[6001]) # RingBellFinish
        # Voice VasaraChen 00001349
        self.set_effect(trigger_ids=[7100])
        # Voice VasaraChen 00001350
        self.set_effect(trigger_ids=[7101])
        # Voice VasaraChen 00001351
        self.set_effect(trigger_ids=[7102])
        # Voice VasaraChen 00001374
        self.set_effect(trigger_ids=[7103])
        self.set_effect(trigger_ids=[7200]) # Voice Speenchi 03000902
        self.set_effect(trigger_ids=[7201]) # Voice Speenchi 03000903
        self.set_effect(trigger_ids=[7202]) # Voice Speenchi 03000904
        self.set_effect(trigger_ids=[7203]) # Voice Speenchi 03000905
        self.set_effect(trigger_ids=[7204]) # Voice Speenchi 03000906
        self.set_effect(trigger_ids=[7205]) # Voice Speenchi 03000907
        self.set_effect(trigger_ids=[7206]) # Voice Speenchi 03000908
        self.set_effect(trigger_ids=[7207]) # Voice Speenchi 03000909
        self.set_effect(trigger_ids=[7208]) # Voice Speenchi 03000910
        self.set_effect(trigger_ids=[7209]) # Voice Speenchi 03000911
        self.set_effect(trigger_ids=[7210]) # Voice Speenchi 03000912
        self.set_effect(trigger_ids=[7211]) # Voice Speenchi 03000913

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return LodingDelay01(self.ctx)


class LodingDelay01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[9900], skill_id=70000093, level=1)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.select_camera(trigger_id=500)

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
        if self.wait_tick(wait_tick=4000):
            return LookAround03(self.ctx)


class LookAround03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=511)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return LookAround04(self.ctx)


class LookAround04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=502)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return TalkKay03(self.ctx)


class TalkKay03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=13000.0)
        self.set_effect(trigger_ids=[7205], visible=True) # Voice Speenchi 03000907
        self.set_dialogue(type=2, spawn_id=11001626, script='$63000020_CS__BATTLE01__0$', time=7) # Voice 03000907
        self.set_skip(state=TalkKay04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return TalkKay04(self.ctx)


class TalkKay04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7205]) # Voice Speenchi 03000907
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return TalkKay10(self.ctx)


class TalkKay10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001626, script='$63000020_CS__BATTLE01__1$', time=8) # Voice 03000908
        self.set_effect(trigger_ids=[7206], visible=True) # Voice Speenchi 03000908
        self.set_skip(state=TalkKay11)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return TalkKay11(self.ctx)


class TalkKay11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Idle_A')
        self.set_effect(trigger_ids=[7206]) # Voice Speenchi 03000908
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FirstChampoin01(self.ctx)


class FirstChampoin01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=600)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return FirstChampoin02(self.ctx)


class FirstChampoin02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=601)
        self.spawn_monster(spawn_ids=[901], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return FirstChampoin03(self.ctx)


class FirstChampoin03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=901, patrol_name='MS2PatrolData_900')
        self.set_dialogue(type=2, spawn_id=11001626, script='$63000020_CS__BATTLE01__2$', time=4) # Voice 03000909
        self.set_effect(trigger_ids=[7207], visible=True) # Voice Speenchi 03000909

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return FirstChampoin04(self.ctx)


class FirstChampoin04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=901, patrol_name='MS2PatrolData_901')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return FirstChampoin05(self.ctx)


class FirstChampoin05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7207]) # Voice Speenchi 03000909
        self.remove_cinematic_talk()
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FirstChampoin06(self.ctx)


class FirstChampoin06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=63000020, portal_id=2)
        self.destroy_monster(spawn_ids=[901])
        self.spawn_monster(spawn_ids=[911], auto_target=False)
        self.select_camera(trigger_id=700)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FirstBattle01(self.ctx)


class FirstBattle01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Talk_A')
        self.set_dialogue(type=2, spawn_id=11001626, script='$63000020_CS__BATTLE01__3$', time=5) # Voice 03000912
        self.set_effect(trigger_ids=[7210], visible=True) # Voice Speenchi 03000912
        self.set_skip(state=FirstBattle02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return FirstBattle02(self.ctx)


class FirstBattle02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7210]) # Voice Speenchi 03000912
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=700, enable=False)
        self.set_agent(trigger_ids=[8000])
        self.set_agent(trigger_ids=[8001])
        self.set_agent(trigger_ids=[8002])
        self.set_agent(trigger_ids=[8003])
        self.set_agent(trigger_ids=[8004])
        self.set_agent(trigger_ids=[8005])
        self.set_agent(trigger_ids=[8006])
        self.set_agent(trigger_ids=[8007])
        self.set_agent(trigger_ids=[8008])
        self.set_effect(trigger_ids=[6000], visible=True) # RingBellStart

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FirstBattle03(self.ctx)


class FirstBattle03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=10025010, text_id=10025010) # 가이드 : 폭주기관차 실바 쓰러트리기
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[911]):
            return Delay01(self.ctx)


class Delay01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6001], visible=True) # RingBellFinish
        self.set_effect(trigger_ids=[5001], visible=True) # 미션 완료 사운드 이펙트
        self.hide_guide_summary(entity_id=10025010)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return SecondChampoin01(self.ctx)


class SecondChampoin01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[600,601], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return SecondChampoin02(self.ctx)


class SecondChampoin02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[902], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return SecondChampoin03(self.ctx)


class SecondChampoin03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=902, patrol_name='MS2PatrolData_900')
        self.set_dialogue(type=2, spawn_id=11001626, script='$63000020_CS__BATTLE01__4$', time=4) # Voice 03000910
        self.set_effect(trigger_ids=[7208], visible=True) # Voice Speenchi 03000910

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return SecondChampoin04(self.ctx)


class SecondChampoin04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=902, patrol_name='MS2PatrolData_901')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return SecondChampoin05(self.ctx)


class SecondChampoin05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7208]) # Voice Speenchi 03000910
        self.remove_cinematic_talk()
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return SecondChampoin06(self.ctx)


class SecondChampoin06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=63000020, portal_id=2)
        self.destroy_monster(spawn_ids=[902])
        self.spawn_monster(spawn_ids=[912], auto_target=False)
        self.select_camera(trigger_id=700)
        self.set_agent(trigger_ids=[8000], visible=True)
        self.set_agent(trigger_ids=[8001], visible=True)
        self.set_agent(trigger_ids=[8002], visible=True)
        self.set_agent(trigger_ids=[8003], visible=True)
        self.set_agent(trigger_ids=[8004], visible=True)
        self.set_agent(trigger_ids=[8005], visible=True)
        self.set_agent(trigger_ids=[8006], visible=True)
        self.set_agent(trigger_ids=[8007], visible=True)
        self.set_agent(trigger_ids=[8008], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return SecondBattle01(self.ctx)


class SecondBattle01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Talk_A')
        self.set_dialogue(type=2, spawn_id=11001626, script='$63000020_CS__BATTLE01__5$', time=5) # Voice 03000912
        self.set_effect(trigger_ids=[7210], visible=True) # Voice Speenchi 03000912
        self.set_skip(state=SecondBattle02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return SecondBattle02(self.ctx)


class SecondBattle02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7210]) # Voice Speenchi 03000912
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=700, enable=False)
        self.set_agent(trigger_ids=[8000])
        self.set_agent(trigger_ids=[8001])
        self.set_agent(trigger_ids=[8002])
        self.set_agent(trigger_ids=[8003])
        self.set_agent(trigger_ids=[8004])
        self.set_agent(trigger_ids=[8005])
        self.set_agent(trigger_ids=[8006])
        self.set_agent(trigger_ids=[8007])
        self.set_agent(trigger_ids=[8008])
        self.set_effect(trigger_ids=[6000], visible=True) # RingBellStart

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return SecondBattle03(self.ctx)


class SecondBattle03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=10025020, text_id=10025020) # 가이드 : 불멸의 피닉스 쓰러트리기
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[912]):
            return Delay02(self.ctx)


class Delay02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6001], visible=True) # RingBellFinish
        self.set_effect(trigger_ids=[5001], visible=True) # 미션 완료 사운드 이펙트
        self.hide_guide_summary(entity_id=10025020)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return ThirdChampoin01(self.ctx)


class ThirdChampoin01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[600,601], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ThirdChampoin02(self.ctx)


class ThirdChampoin02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[903], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ThirdChampoin03(self.ctx)


class ThirdChampoin03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=903, patrol_name='MS2PatrolData_900')
        self.set_dialogue(type=2, spawn_id=11001626, script='$63000020_CS__BATTLE01__6$', time=5) # Voice 03000911
        self.set_effect(trigger_ids=[7209], visible=True) # Voice Speenchi 03000911

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return ThirdChampoin04(self.ctx)


class ThirdChampoin04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=903, patrol_name='MS2PatrolData_901')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ThirdChampoin05(self.ctx)


class ThirdChampoin05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7209]) # Voice Speenchi 03000911
        self.remove_cinematic_talk()
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ThirdChampoin06(self.ctx)


class ThirdChampoin06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=63000020, portal_id=2)
        self.destroy_monster(spawn_ids=[903])
        self.spawn_monster(spawn_ids=[913], auto_target=False)
        self.select_camera(trigger_id=700)
        self.set_agent(trigger_ids=[8000], visible=True)
        self.set_agent(trigger_ids=[8001], visible=True)
        self.set_agent(trigger_ids=[8002], visible=True)
        self.set_agent(trigger_ids=[8003], visible=True)
        self.set_agent(trigger_ids=[8004], visible=True)
        self.set_agent(trigger_ids=[8005], visible=True)
        self.set_agent(trigger_ids=[8006], visible=True)
        self.set_agent(trigger_ids=[8007], visible=True)
        self.set_agent(trigger_ids=[8008], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ThirdBattle01(self.ctx)


class ThirdBattle01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Talk_A')
        self.set_effect(trigger_ids=[7210], visible=True) # Voice Speenchi 03000912
        self.set_dialogue(type=2, spawn_id=11001626, script='$63000020_CS__BATTLE01__7$', time=5) # Voice 03000912
        self.set_skip(state=ThirdBattle02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return ThirdBattle02(self.ctx)


class ThirdBattle02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7210]) # Voice Speenchi 03000912
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=700, enable=False)
        self.set_agent(trigger_ids=[8000])
        self.set_agent(trigger_ids=[8001])
        self.set_agent(trigger_ids=[8002])
        self.set_agent(trigger_ids=[8003])
        self.set_agent(trigger_ids=[8004])
        self.set_agent(trigger_ids=[8005])
        self.set_agent(trigger_ids=[8006])
        self.set_agent(trigger_ids=[8007])
        self.set_agent(trigger_ids=[8008])
        self.set_effect(trigger_ids=[6000], visible=True) # RingBellStart

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ThirdBattle03(self.ctx)


class ThirdBattle03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=10025030, text_id=10025030) # 가이드 : 롤링 더글라스 쓰러트리기
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[913]):
            return Delay03(self.ctx)


class Delay03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6001], visible=True) # RingBellFinish
        self.set_effect(trigger_ids=[5001], visible=True) # 미션 완료 사운드 이펙트
        self.hide_guide_summary(entity_id=10025030)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return TalkKay20(self.ctx)


class TalkKay20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=503)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return TalkKay21(self.ctx)


class TalkKay21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Talk_A')
        self.select_camera(trigger_id=502)
        self.set_dialogue(type=2, spawn_id=11001626, script='$63000020_CS__BATTLE01__8$', time=9) # Voice 03000913
        self.set_effect(trigger_ids=[7211], visible=True) # Voice Speenchi 03000913
        self.set_skip(state=TalkKay22)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return TalkKay22(self.ctx)


class TalkKay22(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=63000020, portal_id=6)
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_effect(trigger_ids=[7211]) # Voice Speenchi 03000913

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PCFeelDizzy01(self.ctx)


# PC 현기증 Blur
class PCFeelDizzy01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=703)
        self.move_user_path(patrol_name='MS2PatrolData_1000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return PCFeelDizzy02(self.ctx)


class PCFeelDizzy02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$63000020_CS__BATTLE01__9$', time=4)
        self.set_pc_emotion_sequence(sequence_names=['Emotion_Disappoint_A','Emotion_Disappoint_Idle_A'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4200):
            return PCFeelDizzy03(self.ctx)


class PCFeelDizzy03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=705)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return PCFeelDizzy04(self.ctx)


class PCFeelDizzy04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=704)
        self.set_effect(trigger_ids=[7001], visible=True) # VibrateDizzy
        self.add_buff(box_ids=[9900], skill_id=70000094, level=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return PCFeelOkay01(self.ctx)


class PCFeelOkay01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7001]) # VibrateDizzy
        self.add_buff(box_ids=[9900], skill_id=70000096, level=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return PCFeelOkay02(self.ctx)


class PCFeelOkay02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=703)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return PCFeelOkay03(self.ctx)


class PCFeelOkay03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$63000020_CS__BATTLE01__10$', time=4)
        self.set_pc_emotion_sequence(sequence_names=['Bore_C'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return PCFeelOkay04(self.ctx)


class PCFeelOkay04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6000], visible=True) # RingBellStart
        self.select_camera(trigger_id=504)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return TalkKay23(self.ctx)


class TalkKay23(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Talk_A')
        self.set_dialogue(type=2, spawn_id=11001626, script='$63000020_CS__BATTLE01__11$', time=9) # Voice 03000902
        self.set_effect(trigger_ids=[7200], visible=True) # Voice Speenchi 03000902
        self.set_skip(state=TalkKay24)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return TalkKay24(self.ctx)


class TalkKay24(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.move_user(map_id=63000020, portal_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return TalkKay25(self.ctx)


class TalkKay25(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7200]) # Voice Speenchi 03000902
        self.select_camera(trigger_id=710)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return TalkKay26(self.ctx)


class TalkKay26(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Talk_A')
        self.set_dialogue(type=2, spawn_id=11001626, script='$63000020_CS__BATTLE01__12$', time=14) # Voice 03000903
        self.set_effect(trigger_ids=[7201], visible=True) # Voice Speenchi 03000903
        self.set_skip(state=TalkKay27)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=14000):
            return TalkKay27(self.ctx)


class TalkKay27(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_effect(trigger_ids=[7201]) # Voice Speenchi 03000903

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return TalkKay28(self.ctx)


class TalkKay28(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=502)
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Talk_A')
        self.set_dialogue(type=2, spawn_id=11001626, script='$63000020_CS__BATTLE01__13$', time=10) # Voice 03000904
        self.set_effect(trigger_ids=[7202], visible=True) # Voice Speenchi 03000904
        self.set_skip(state=TalkKay29)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return TalkKay29(self.ctx)


class TalkKay29(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7202]) # Voice Speenchi 03000904
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return LastChampoin01(self.ctx)


class LastChampoin01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=601)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return LastChampoin02(self.ctx)


class LastChampoin02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[900], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return LastChampoin03(self.ctx)


class LastChampoin03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Talk_A')
        self.move_npc(spawn_id=900, patrol_name='MS2PatrolData_902')
        self.set_dialogue(type=2, spawn_id=11001626, script='$63000020_CS__BATTLE01__14$', time=11) # Voice 03000905
        self.set_effect(trigger_ids=[7203], visible=True) # Voice Speenchi 03000905

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return LastChampoin04(self.ctx)


class LastChampoin04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=900, sequence_name='Bore_A')
        self.set_skip(state=LastChampoin05)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return LastChampoin05(self.ctx)


class LastChampoin05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=900, patrol_name='MS2PatrolData_901')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return LastChampoin06(self.ctx)


class LastChampoin06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7203]) # Voice Speenchi 03000905
        self.remove_cinematic_talk()
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return LastChampoin07(self.ctx)


class LastChampoin07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=63000020, portal_id=2)
        self.destroy_monster(spawn_ids=[900])
        self.spawn_monster(spawn_ids=[924], auto_target=False)
        self.select_camera(trigger_id=700)
        self.set_agent(trigger_ids=[8000], visible=True)
        self.set_agent(trigger_ids=[8001], visible=True)
        self.set_agent(trigger_ids=[8002], visible=True)
        self.set_agent(trigger_ids=[8003], visible=True)
        self.set_agent(trigger_ids=[8004], visible=True)
        self.set_agent(trigger_ids=[8005], visible=True)
        self.set_agent(trigger_ids=[8006], visible=True)
        self.set_agent(trigger_ids=[8007], visible=True)
        self.set_agent(trigger_ids=[8008], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return LastBattle01(self.ctx)


class LastBattle01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Talk_A')
        self.set_dialogue(type=2, spawn_id=11001626, script='$63000020_CS__BATTLE01__15$', time=7) # Voice 03000906
        self.set_effect(trigger_ids=[7204], visible=True) # Voice Speenchi 03000906
        self.set_skip(state=LastBattle02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return LastBattle02(self.ctx)


# 조정 필요
class LastBattle02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7204]) # Voice Speenchi 03000906
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.select_camera(trigger_id=701)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return LastBattle03(self.ctx)


class LastBattle03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$63000020_CS__BATTLE01__16$', time=3)
        self.set_pc_emotion_sequence(sequence_names=['Striker_Bore_A'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return LastBattle04(self.ctx)


class LastBattle04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[924])
        self.spawn_monster(spawn_ids=[910], auto_target=False)
        self.select_camera(trigger_id=702)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return TalkChen10(self.ctx)


class TalkChen10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001547, script='$63000020_CS__BATTLE01__17$', time=4) # Voice 00001349
        # Voice VasaraChen 00001349
        self.set_effect(trigger_ids=[7100], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return TalkChen11(self.ctx)


class TalkChen11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Voice VasaraChen 00001349
        self.set_effect(trigger_ids=[7100])
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return BattleStart01(self.ctx)


class BattleStart01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=702, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_effect(trigger_ids=[6000], visible=True) # RingBellStart

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return BattleStart02(self.ctx)


class BattleStart02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[8000])
        self.set_agent(trigger_ids=[8001])
        self.set_agent(trigger_ids=[8002])
        self.set_agent(trigger_ids=[8003])
        self.set_agent(trigger_ids=[8004])
        self.set_agent(trigger_ids=[8005])
        self.set_agent(trigger_ids=[8006])
        self.set_agent(trigger_ids=[8007])
        self.set_agent(trigger_ids=[8008])
        self.show_guide_summary(entity_id=10025040, text_id=10025040) # 가이드 : 바사라 첸 쓰러트리기
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return CameraAct01(self.ctx)


class CameraAct01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return CameraAct02(self.ctx)


class CameraAct02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=10025040)
        self.move_user(map_id=63000020, portal_id=4)
        self.destroy_monster(spawn_ids=[910])
        self.spawn_monster(spawn_ids=[920], auto_target=False)
        self.select_camera(trigger_id=800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return PCAttack01(self.ctx)


class PCAttack01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_pc_emotion_sequence(sequence_names=['Knuckle_Attack_Idle_A'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=900):
            return PCAttack02(self.ctx)


class PCAttack02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_sequence(sequence_names=['Striker_Event_01'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=900):
            return KnockBack01(self.ctx)


class KnockBack01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=920, sequence_name='Attack_01_H')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return KnockBack02(self.ctx)


class KnockBack02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7000], enable=True)
        self.select_camera(trigger_id=801)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=900):
            return KnockBack03(self.ctx)


class KnockBack03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_loop(sequence_name='Push_A', duration=3000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return BlurAct01(self.ctx)


# PC 1인칭 시점 Blur 연출
class BlurAct01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=802) # FirstPerspective
        self.add_buff(box_ids=[9900], skill_id=70000094, level=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return BlurAct02(self.ctx)


class BlurAct02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=803) # FirstPerspective
        self.set_effect(trigger_ids=[7001], visible=True) # VibrateDizzy

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return BlurAct03(self.ctx)


class BlurAct03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return BlurAct04(self.ctx)


class BlurAct04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[9900], skill_id=70000095, level=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return BlurAct05(self.ctx)


class BlurAct05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=805)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1200):
            return BlurAct06(self.ctx)


class BlurAct06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return BlurAct07(self.ctx)


class BlurAct07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_loop(sequence_name='Emotion_Disappoint_Idle_A', duration=24000.0)
        self.set_effect(trigger_ids=[7001]) # VibrateDizzy
        self.add_buff(box_ids=[9900], skill_id=70000096, level=1)
        self.select_camera(trigger_id=806)
        self.destroy_monster(spawn_ids=[920])
        self.spawn_monster(spawn_ids=[922], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return BlurAct08(self.ctx)


class BlurAct08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_npc(spawn_id=922, patrol_name='MS2PatrolData_920')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return TalkChen01(self.ctx)


class TalkChen01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001547, script='$63000020_CS__BATTLE01__18$', time=5) # Voice 00001350
        # Voice VasaraChen 00001350
        self.set_effect(trigger_ids=[7101], visible=True)
        self.set_skip(state=TalkChen02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return TalkChen02(self.ctx)


class TalkChen02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Voice VasaraChen 00001350
        self.set_effect(trigger_ids=[7101])
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return TalkChen03(self.ctx)


class TalkChen03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001547, script='$63000020_CS__BATTLE01__19$', time=4) # Voice 00001374  Think
        # Voice VasaraChen 00001374
        self.set_effect(trigger_ids=[7103], visible=True)
        self.set_skip(state=TalkChen04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return TalkChen04(self.ctx)


class TalkChen04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Voice VasaraChen 00001374
        self.set_effect(trigger_ids=[7103])
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return TalkChen05(self.ctx)


class TalkChen05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001547, script='$63000020_CS__BATTLE01__20$', time=4) # Voice 00001351
        # Voice VasaraChen 00001351
        self.set_effect(trigger_ids=[7102], visible=True)
        self.set_skip(state=TalkChen06)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return TalkChen06(self.ctx)


class TalkChen06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.destroy_monster(spawn_ids=[922])
        self.spawn_monster(spawn_ids=[923], auto_target=False)
        # Voice VasaraChen 00001351
        self.set_effect(trigger_ids=[7102])
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return LastAttack00(self.ctx)


class LastAttack00(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=923, sequence_name='Attack_02_G', duration=2000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return LastAttack01(self.ctx)


# Skill Effect Attack 연출
class LastAttack01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.add_buff(box_ids=[9900], skill_id=70000095, level=1)
        self.select_camera(trigger_id=807) # FirstPerspective Hit

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return LastAttack02(self.ctx)


class LastAttack02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=808) # FirstPerspective Hit

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=900):
            return LastAttack03(self.ctx)


class LastAttack03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=923, sequence_name='Attack_03_G')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=700):
            # 피격 당하는 순간
            return PCFainted01(self.ctx)


class PCFainted01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[9900], skill_id=70000096, level=1)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return PCFainted02(self.ctx)


class PCFainted02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[9900], skill_id=70000095, level=1)
        self.select_camera(trigger_id=804) # FirstPerspective Down

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return PCFainted03(self.ctx)


class PCFainted03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Bore_A') # WeiHong

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return PlayerDown01(self.ctx)


class PlayerDown01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return PlayerDown02(self.ctx)


class PlayerDown02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[9900], skill_id=70000096, level=1)
        self.move_user(map_id=63000020, portal_id=5)
        self.destroy_monster(spawn_ids=[923])
        self.spawn_monster(spawn_ids=[921], auto_target=False)
        self.select_camera(trigger_id=810)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return PlayerDown03(self.ctx)


class PlayerDown03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_loop(sequence_name='Down_Idle_A', duration=16000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return PlayerDown04(self.ctx)


class PlayerDown04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_npc(spawn_id=921, patrol_name='MS2PatrolData_921')
        self.set_effect(trigger_ids=[6001], visible=True) # RingBellFinish

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PlayerDown05(self.ctx)


class PlayerDown05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=811)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return PlayerDown06(self.ctx)


class PlayerDown06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=812)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return PlayerDown07(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[921])


class PlayerDown07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.select_camera(trigger_id=812, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return MoveToNextMap01(self.ctx)


class MoveToNextMap01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(map_id=63000021, portal_id=1, box_id=9900)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[9900]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
