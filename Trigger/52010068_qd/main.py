""" trigger/52010068_qd/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001])
        self.set_effect(trigger_ids=[5002])

    def on_tick(self) -> trigger_api.Trigger:
        if not self.quest_user_detected(box_ids=[2001], quest_ids=[20002391], quest_states=[3]):
            # 인트로 퀘스트
            return 틴차이_준타_스폰01(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[50100420], quest_states=[3]):
            return Orde_Out_Effect(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[50100420], quest_states=[2]):
            return Orde_Out_Effect(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[50100420], quest_states=[1]):
            return Orde_Out_Effect(self.ctx)
        """
        if self.quest_user_detected(box_ids=[2001], quest_ids=[50100640], quest_states=[2]):
            return 챕터10에필로그연출01(self.ctx)
        """
        if self.quest_user_detected(box_ids=[2001], quest_ids=[50100400], quest_states=[3]):
            return Orde_In_Effect(self.ctx)


class 틴차이_준타_스폰01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[102])
        self.spawn_monster(spawn_ids=[103])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[50100420], quest_states=[3]):
            return Orde_Out_Effect(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[50100420], quest_states=[2]):
            return Orde_Out_Effect(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[50100420], quest_states=[1]):
            return Orde_Out_Effect(self.ctx)
        """
        if self.quest_user_detected(box_ids=[2001], quest_ids=[50100640], quest_states=[2]):
            return 챕터10에필로그연출01(self.ctx)
        """
        if self.quest_user_detected(box_ids=[2001], quest_ids=[50100400], quest_states=[3]):
            return Orde_In_Effect(self.ctx)


class Orde_In_Effect(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_effect(trigger_ids=[5001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Orde_In(self.ctx)


class Orde_In(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Orde_In_Turn(self.ctx)


class Orde_In_Turn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=600)
        self.set_effect(trigger_ids=[5001], visible=True)
        self.set_npc_rotation(spawn_id=101, rotation=-45.0)
        self.add_cinematic_talk(npc_id=11004033, illust_id='Orde_normal', msg='$52010068_QD__MAIN__0$', align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Orde_In_Talk(self.ctx)


class Orde_In_Talk(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='IceSphere_A')
        self.add_cinematic_talk(npc_id=11004033, illust_id='Orde_normal', msg='$52010068_QD__MAIN__1$', align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Orde_In_Talk_End(self.ctx)


class Orde_In_Talk_End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Orde_In_ReTurn(self.ctx)


class Orde_In_ReTurn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_rotation(spawn_id=101, rotation=360.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[50100420], quest_states=[3]):
            return Orde_Out_Effect(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[50100420], quest_states=[2]):
            return Orde_Out_Effect(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[50100420], quest_states=[1]):
            return Orde_Out_Effect(self.ctx)


class Orde_Out_Effect(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Wizard_Teleport_A')
        self.add_balloon_talk(spawn_id=101, msg='$52010068_QD__MAIN__2$', duration=2800)
        self.set_effect(trigger_ids=[5002], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Orde_Out(self.ctx)


class Orde_Out(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101])
        self.set_effect(trigger_ids=[5002])


class 챕터10에필로그연출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=10, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 챕터10에필로그연출02(self.ctx)


class 챕터10에필로그연출02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=9, script='큰 희생이 있었지만, 우리는 $npc:11001698$를 상대로 승리를 얻었다.\\n메이플월드를 공격한 그들에게 죄값을 치르게 만든것이다.')
        self.set_skip(state=챕터10에필로그연출02스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 챕터10에필로그연출02스킵(self.ctx)


class 챕터10에필로그연출02스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 챕터10에필로그연출03(self.ctx)


class 챕터10에필로그연출03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='비록 $npc:11001698$는 무사히 도망쳤지만, \\n그녀 스스로의 의지로 도망친것은 아니었다.')
        self.set_skip(state=챕터10에필로그연출03스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 챕터10에필로그연출03스킵(self.ctx)


class 챕터10에필로그연출03스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 챕터10에필로그연출05(self.ctx)


class 챕터10에필로그연출05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='오히려 $npc:11001698$는 이번 전투에서 자신의 요새를 잃고 말았다.')
        self.set_skip(state=챕터10에필로그연출05스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 챕터10에필로그연출05스킵(self.ctx)


class 챕터10에필로그연출05스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 챕터10에필로그연출05b(self.ctx)


class 챕터10에필로그연출05b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 챕터10에필로그연출06(self.ctx)


class 챕터10에필로그연출06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=90000, enable=True) # 마드리아 고조 브금
        self.set_dialogue(type=2, spawn_id=11001820, script='$52010068_QD__MAIN__3$', time=6)
        self.set_onetime_effect(id=2007, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_01_00002007.xml')
        self.set_skip(state=챕터10에필로그연출06스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 챕터10에필로그연출06스킵(self.ctx)


class 챕터10에필로그연출06스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 챕터10에필로그연출07(self.ctx)


class 챕터10에필로그연출07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001820, script='$52010068_QD__MAIN__4$', time=6)
        self.set_onetime_effect(id=2008, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_02_00002008.xml')
        self.set_skip(state=챕터10에필로그연출07스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 챕터10에필로그연출07스킵(self.ctx)


class 챕터10에필로그연출07스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 챕터10에필로그연출08(self.ctx)


class 챕터10에필로그연출08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001820, script='$52010068_QD__MAIN__5$', time=9)
        self.set_onetime_effect(id=2009, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_03_00002009.xml')
        self.set_skip(state=챕터10에필로그연출08스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return 챕터10에필로그연출08스킵(self.ctx)


class 챕터10에필로그연출08스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 챕터10에필로그연출09(self.ctx)


class 챕터10에필로그연출09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001820, script='$52010068_QD__MAIN__6$', time=5)
        self.set_onetime_effect(id=2009, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_03_00002009.xml')
        self.set_skip(state=챕터10에필로그연출9스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 챕터10에필로그연출9스킵(self.ctx)


class 챕터10에필로그연출9스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 챕터10에필로그연출10(self.ctx)


class 챕터10에필로그연출10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11001820, script='$52010068_QD__MAIN__7$', time=5)
        self.set_onetime_effect(id=2010, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_04_00002010.xml')
        self.set_skip(state=챕터10에필로그연출10스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 챕터10에필로그연출10스킵(self.ctx)


class 챕터10에필로그연출10스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 챕터10에필로그연출11(self.ctx)


class 챕터10에필로그연출11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001820, script='$52010068_QD__MAIN__8$', time=5)
        self.set_onetime_effect(id=2011, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_05_00002011.xml')
        self.set_skip(state=챕터10에필로그연출11스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 챕터10에필로그연출11스킵(self.ctx)


class 챕터10에필로그연출11스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 챕터10에필로그연출12(self.ctx)


class 챕터10에필로그연출12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001820, script='$52010068_QD__MAIN__9$', time=5)
        self.set_onetime_effect(id=2011, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_05_00002011.xml')
        self.set_skip(state=챕터10에필로그연출12스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 챕터10에필로그연출12스킵(self.ctx)


class 챕터10에필로그연출12스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 챕터10에필로그연출13(self.ctx)


class 챕터10에필로그연출13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001820, script='$52010068_QD__MAIN__10$', time=5)
        self.set_onetime_effect(id=2011, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_05_00002011.xml')
        self.set_skip(state=챕터10에필로그연출13스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 챕터10에필로그연출13스킵(self.ctx)


class 챕터10에필로그연출13스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 챕터10에필로그연출13_b(self.ctx)


class 챕터10에필로그연출13_b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11001820, script='$52010068_QD__MAIN__11$', time=5)
        self.set_onetime_effect(id=2012, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_06_00002012.xml')
        self.set_skip(state=챕터10에필로그연출13b스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 챕터10에필로그연출13b스킵(self.ctx)


class 챕터10에필로그연출13b스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 챕터10에필로그연출14(self.ctx)


class 챕터10에필로그연출14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001820, script='$52010068_QD__MAIN__12$', time=5)
        self.set_onetime_effect(id=2013, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_07_00002013.xml')
        self.set_skip(state=챕터10에필로그연출14스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 챕터10에필로그연출14스킵(self.ctx)


class 챕터10에필로그연출14스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 챕터10에필로그연출15(self.ctx)


class 챕터10에필로그연출15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001820, script='$52010068_QD__MAIN__13$', time=6)
        self.set_onetime_effect(id=2014, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_08_00002014.xml')
        self.set_skip(state=챕터10에필로그연출15스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 챕터10에필로그연출15스킵(self.ctx)


class 챕터10에필로그연출15스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 챕터10에필로그연출16(self.ctx)


class 챕터10에필로그연출16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001820, script='$52010068_QD__MAIN__14$', time=5)
        self.set_onetime_effect(id=2015, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_09_00002015.xml')
        self.set_skip(state=챕터10에필로그연출16스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 챕터10에필로그연출16스킵(self.ctx)


class 챕터10에필로그연출16스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 챕터10에필로그연출17(self.ctx)


class 챕터10에필로그연출17(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 챕터10에필로그연출18(self.ctx)


class 챕터10에필로그연출18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$npc:11001698$는 그녀의 용을 타고 날아올랐다\\n그리고 이 것이 마드라칸 요새의 최후였다.')
        self.set_skip(state=챕터10에필로그연출18스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 챕터10에필로그연출18스킵(self.ctx)


class 챕터10에필로그연출18스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 챕터10에필로그연출18b(self.ctx)


class 챕터10에필로그연출18b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$npc:11001698$는 분명 다시 돌아올 것이다.\\n그리고 또다시 서로에게 소중한 존재들을 빼앗을지도 모른다.')
        self.set_skip(state=챕터10에필로그연출18b스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 챕터10에필로그연출18b스킵(self.ctx)


class 챕터10에필로그연출18b스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 챕터10에필로그연출19(self.ctx)


class 챕터10에필로그연출19(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='그렇지만, 할 수 있다면 $npc:11001698$와 싸우지 않아도 될 방법을 찾고자 한다.\\n복수의 나선은 결국 서로의 모든것을 파괴할것이기 때문이다.')
        self.set_skip(state=챕터10에필로그연출19스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 챕터10에필로그연출19스킵(self.ctx)


class 챕터10에필로그연출19스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 챕터10에필로그연출20(self.ctx)


class 챕터10에필로그연출20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='그리고 나는 어떤 방법으로든 테룬칼리브들이 살아있다고 굳게 믿고 있다.\\n그들이 나를 살렸듯 그들 스스로 어떻게 살아날 방법을 찾았을거라 믿고 싶다.')
        self.set_skip(state=챕터10에필로그연출20스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 챕터10에필로그연출20스킵(self.ctx)


class 챕터10에필로그연출20스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 챕터10에필로그연출21(self.ctx)


class 챕터10에필로그연출21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='하여, 나는 블랙 샤드의 폭심지, \'아이 오브 라펜타\'의 수색과\\n라펜샤드의 조사에 최선을 다할 것이라고 다짐했다.')
        self.set_skip(state=챕터10에필로그연출22)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 챕터10에필로그연출22(self.ctx)


class 챕터10에필로그연출22(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=10, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_user(map_id=52010068, portal_id=2)


initial_state = Ready
