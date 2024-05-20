""" trigger/63000077_cs/63000077_main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class 준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.spawn_monster(spawn_ids=[102], auto_target=False)
        self.set_actor(trigger_id=3001, initial_sequence='0') # 아빠끄기

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[30000379], quest_states=[3]):
            # 크리스마스 스토리 퀘스트 모두 함께 파티를까지 10종 전체 완료시 일퀘 수행 상태로 만들기
            return 일반사냥(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[30000378], quest_states=[2]):
            return 일반사냥(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[30000378], quest_states=[1]):
            return 수락_01_30000378(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[30000377], quest_states=[3]):
            return 완료_01_30000377(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[30000377], quest_states=[2]):
            return 화난보보스_01(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[30000377], quest_states=[1]):
            return 잠시대기_01(self.ctx)
        if self.user_detected(box_ids=[701]):
            return 일반사냥(self.ctx)


class 수락_01_30000378(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 수락_02_30000378(self.ctx)


class 수락_02_30000378(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[106,108], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 에블린일기_01(self.ctx)


class 완료_01_30000377(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 완료_02_30000377(self.ctx)


class 완료_02_30000377(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[106,108], auto_target=False)
        self.reset_camera()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 클라우스대화_05(self.ctx)


class 잠시대기_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_actor(trigger_id=3001, visible=True, initial_sequence='Talk_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 잠시대기_02(self.ctx)


class 잠시대기_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=8001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 보보스의오해_01(self.ctx)


class 보보스의오해_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_scene_skip(state=화난보보스_01, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 보보스의오해_02(self.ctx)


class 보보스의오해_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8002], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 보보스의오해_03(self.ctx)


class 보보스의오해_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 미안해… 소원… 들어줘야 하니까.\n내가 루돌프 되면 꼭 내려줄게.
        self.add_cinematic_talk(npc_id=11004373, msg='$63000077_CS__63000077_MAIN__0$', duration=3500, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 보보스의오해_04(self.ctx)


class 보보스의오해_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8003], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 보보스의오해_05(self.ctx)


class 보보스의오해_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=102, msg='$63000077_CS__63000077_MAIN__1$', duration=2000) # 으아…오…옷…어…오우

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 보보스의오해_06(self.ctx)


class 보보스의오해_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=8004)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 보보스의오해_07(self.ctx)


class 보보스의오해_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_sequence(sequence_names=['Emotion_Angry_A'])
        self.add_cinematic_talk(npc_id=0, msg='$63000077_CS__63000077_MAIN__2$', duration=2800, align=Align.Right) # 이봐, 무슨 짓이야! 당장 그만둬!
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 보보스의오해_08(self.ctx)


class 보보스의오해_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=8005)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 보보스의오해_09(self.ctx)


class 보보스의오해_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 응…? 나…는 소원 들어주고 있어.\n$npcName:11004356$의 크리스마스 소원.
        self.add_cinematic_talk(npc_id=11004373, msg='$63000077_CS__63000077_MAIN__3$', duration=3500, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 보보스의오해_10(self.ctx)


class 보보스의오해_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=8006)
        self.face_emotion(emotion_name='Angry')
        self.move_user_path(patrol_name='MS2PatrolData_2002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 보보스의오해_11(self.ctx)


class 보보스의오해_11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # $npcName:11004356$의 소원은 그런 게 아냐!\n$npcName:11004368$$pp:는,은$ $npcName:11004356$의 소중한 가족이라고! 당장 내려줘!
        self.add_cinematic_talk(npc_id=0, msg='$63000077_CS__63000077_MAIN__4$', duration=4000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4500):
            return 보보스의오해_12(self.ctx)


class 보보스의오해_12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=8005)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 보보스의오해_13(self.ctx)


class 보보스의오해_13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004373, msg='$63000077_CS__63000077_MAIN__5$', duration=2500, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 보보스의오해_14(self.ctx)


class 보보스의오해_14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # $npcName:11004356$ 아빠, 여기 있어야 된다.\n$npcName:11004373$$pp:는,은$ 착한 일을 하는 거다.
        self.add_cinematic_talk(npc_id=11004373, msg='$63000077_CS__63000077_MAIN__6$', duration=3500, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 보보스의오해_15(self.ctx)


class 보보스의오해_15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=8006)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 보보스의오해_16(self.ctx)


class 보보스의오해_16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.face_emotion(emotion_name='Trigger_disappoint')
        self.add_cinematic_talk(npc_id=0, msg='$63000077_CS__63000077_MAIN__7$', duration=2500, align=Align.Right) # 정말 말이 안 통하는 녀석이잖아.

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 보보스의오해_17(self.ctx)


class 보보스의오해_17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.face_emotion(emotion_name='Trigger_panic')
        self.add_cinematic_talk(npc_id=0, msg='$63000077_CS__63000077_MAIN__8$', duration=2500, align=Align.Right) # 도대체 무슨 소릴 하는 거야?

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 보보스의오해_18(self.ctx)

    def on_exit(self) -> None:
        self.face_emotion()


class 보보스의오해_18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=8005)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 보보스의오해_19(self.ctx)


class 보보스의오해_19(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # $npcName:11004373$, 착한 일 하고 산타 할아버지한테 인정 받을 거다.
        self.add_cinematic_talk(npc_id=11004373, msg='$63000077_CS__63000077_MAIN__9$', duration=2500, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 보보스의오해_20(self.ctx)


class 보보스의오해_20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 루돌프 돼서, 행복해지고…\n$npcName:11004356$이랑도 같이 놀 거야.
        self.add_cinematic_talk(npc_id=11004373, msg='$63000077_CS__63000077_MAIN__10$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 보보스의오해_21(self.ctx)


class 보보스의오해_21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8007], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 보보스의오해_22(self.ctx)


class 보보스의오해_22(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004373, msg='$63000077_CS__63000077_MAIN__11$', duration=2000, align=Align.Right) # 날 방해하면…

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 보보스의오해_23(self.ctx)


class 보보스의오해_23(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # &lt;font size='40'&gt;때릴 거다!&lt;/font&gt;
        self.add_cinematic_talk(npc_id=11004373, msg='$63000077_CS__63000077_MAIN__12$', duration=2000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 화난보보스_01(self.ctx)


class 화난보보스_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 화난보보스_02(self.ctx)


class 화난보보스_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()
        self.destroy_monster(spawn_ids=[101,102])
        self.spawn_monster(spawn_ids=[220], auto_target=False)
        self.spawn_monster(spawn_ids=[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 화난보보스_03(self.ctx)


class 화난보보스_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[30000377], quest_states=[2]):
            return 패배한보보스_01(self.ctx)


class 일반사냥(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=3001, initial_sequence='0') # 아빠액터끄기
        self.destroy_monster(spawn_ids=[101,102])
        self.spawn_monster(spawn_ids=[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216], auto_target=False) # 보보스제외, 일반몹만 소환

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class 패배한보보스_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 패배한보보스_02(self.ctx)


class 패배한보보스_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,220])
        self.spawn_monster(spawn_ids=[106], auto_target=False)
        self.spawn_monster(spawn_ids=[107], auto_target=False)
        self.set_npc_emotion_loop(spawn_id=106, sequence_name='Cry_A', duration=35000.0)
        self.set_actor(trigger_id=3001, initial_sequence='Talk_A')
        self.move_user(map_id=63000077, portal_id=4)
        self.select_camera(trigger_id=8008)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 패배한보보스_03(self.ctx)


class 패배한보보스_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_scene_skip(state=클라우스대화_03, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 클라우스대화_01(self.ctx)


class 클라우스대화_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004368, msg='$63000077_CS__63000077_MAIN__13$', duration=2500, align=Align.Left) # 도와주셔서 감사합니다!

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 클라우스대화_02(self.ctx)


class 클라우스대화_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004368, msg='$63000077_CS__63000077_MAIN__14$', duration=2500, align=Align.Left) # 그런데 누구……?

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 클라우스대화_03(self.ctx)


class 클라우스대화_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 클라우스대화_04(self.ctx)


class 클라우스대화_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[107])
        self.spawn_monster(spawn_ids=[108], auto_target=False)
        self.reset_camera()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 클라우스대화_05(self.ctx)


class 클라우스대화_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[30000378], quest_states=[1]):
            return 에블린일기_01(self.ctx)


class 에블린일기_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 에블린일기_02(self.ctx)


class 에블린일기_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # &lt;FONT color='#ffd200'&gt;누군가의 일기장 52페이지&lt;/FONT&gt;\n아빠 미워. 그깟 꽃이 뭐라고 나를 그렇게 혼낸 거야? \n화단 하나 관리 못 했다고 세상이 뒤집히는 것도 아닌데.\n꽃이 나보다 소중하면, 내 눈에 띄지 말고 쭉 정원에서 살아! $npcName:11004368$씨!
        self.set_cinematic_ui(type=9, script='$63000077_CS__63000077_MAIN__15$')
        self.move_user(map_id=63000077, portal_id=4)
        self.select_camera(trigger_id=8008)
        self.set_scene_skip(state=업적_01, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 에블린일기_03(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=2)


class 에블린일기_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=5, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 다시만난가족_01(self.ctx)


class 다시만난가족_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 제가 $npcName:11004356$의 마음을 아프게 한 것도 사실이고,\n제 딸 $npcName:11004356$의 마음을 달래주려는 순진한 $npcName:11004373$의 부탁이니…
        self.add_cinematic_talk(npc_id=11004368, msg='$63000077_CS__63000077_MAIN__16$', duration=3500, illust_id='June_normal', align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 다시만난가족_02(self.ctx)


class 다시만난가족_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 잠깐 나무 위에 올라가 있는 것도 나쁘지 않겠다 싶었답니다
        self.add_cinematic_talk(npc_id=11004368, msg='$63000077_CS__63000077_MAIN__17$', duration=3000, illust_id='June_normal', align=Align.Left)
        self.spawn_monster(spawn_ids=[103,104,105], auto_target=False)
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_2003')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 다시만난가족_03(self.ctx)

    def on_exit(self) -> None:
        self.move_npc(spawn_id=108, patrol_name='MS2PatrolData_2006')


class 다시만난가족_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004356, msg='$63000077_CS__63000077_MAIN__18$', duration=2000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 다시만난가족_04(self.ctx)


class 다시만난가족_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8009], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 다시만난가족_05(self.ctx)


class 다시만난가족_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 그건 그냥 투정이었어.\n내 소원은 그런 게 아니란 말이에요!
        self.add_cinematic_talk(npc_id=11004356, msg='$63000077_CS__63000077_MAIN__19$', duration=3500, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 다시만난가족_06(self.ctx)


class 다시만난가족_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=8012)
        self.add_cinematic_talk(npc_id=11004373, msg='$63000077_CS__63000077_MAIN__20$', duration=2000, align=Align.Left) # 으응???

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 다시만난가족_07(self.ctx)


class 다시만난가족_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=106, patrol_name='MS2PatrolData_2007')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 다시만난가족_08(self.ctx)


class 다시만난가족_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # $npcName:11004356$…소원 아니야?\n내가 잘못한거야…?
        self.add_cinematic_talk(npc_id=11004373, msg='$63000077_CS__63000077_MAIN__21$', duration=3500, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 다시만난가족_09(self.ctx)


class 다시만난가족_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=8011)
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_2008')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 다시만난가족_10(self.ctx)


class 다시만난가족_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 보…?\n그날 밤 내 얘길 듣고 간 게 역시 너였구나.
        self.add_cinematic_talk(npc_id=11004356, msg='$63000077_CS__63000077_MAIN__22$', duration=3500, illust_id='Evelyn_glad', align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 다시만난가족_11(self.ctx)


class 다시만난가족_11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_2004')
        self.move_npc(spawn_id=105, patrol_name='MS2PatrolData_2005')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 다시만난가족_12(self.ctx)


class 다시만난가족_12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 미안…미안해…!\n소원을 들어주고… 행복하게 해주고 싶었는데…!
        self.add_cinematic_talk(npc_id=11004373, msg='$63000077_CS__63000077_MAIN__23$', duration=4000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4500):
            return 다시만난가족_13(self.ctx)


class 다시만난가족_13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # $npcName:11004373$$pp:가,이$… 너무 미안해…!
        self.add_cinematic_talk(npc_id=11004373, msg='$63000077_CS__63000077_MAIN__24$', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 다시만난가족_14(self.ctx)


class 다시만난가족_14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=8011)
        # 아니야, 털북숭이. 미안해 할 필요 없어.\n$npcName:11004356$의 소원은 따로 있으니까
        self.add_cinematic_talk(npc_id=11004361, msg='$63000077_CS__63000077_MAIN__25$', duration=4000, illust_id='Aiden_smile', align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4500):
            return 다시만난가족_15(self.ctx)


class 다시만난가족_15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 그래. 진짜 소원을 말하면, 그걸 들어주렴.
        self.add_cinematic_talk(npc_id=11004365, msg='$63000077_CS__63000077_MAIN__26$', duration=3500, illust_id='Mia_happy', align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 다시만난가족_16(self.ctx)


class 다시만난가족_16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004356, msg='$63000077_CS__63000077_MAIN__27$', duration=2000, illust_id='Evelyn_normal', align=Align.Right) # ……

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 다시만난가족_17(self.ctx)


class 다시만난가족_17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 미안해요, 모두.\n내가 부린 투정 때문에… 모두 너무 고생했어요.
        self.add_cinematic_talk(npc_id=11004356, msg='$63000077_CS__63000077_MAIN__28$', duration=3500, illust_id='Evelyn_sad', align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 다시만난가족_18(self.ctx)


class 다시만난가족_18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 그래서, 우리 $npcName:11004356$의 진짜 크리스마스 소원은 뭐지?
        self.add_cinematic_talk(npc_id=11004368, msg='$63000077_CS__63000077_MAIN__29$', duration=3000, illust_id='June_smile', align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 다시만난가족_19(self.ctx)


class 다시만난가족_19(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 우리 가족 모두 함께 모여서…\n행복한 크리스마스 파티를 하는 거예요
        self.add_cinematic_talk(npc_id=11004356, msg='$63000077_CS__63000077_MAIN__30$', duration=3500, illust_id='Evelyn_glad', align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 다시만난가족_20(self.ctx)


class 다시만난가족_20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8013], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 업적_01(self.ctx)


class 업적_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.set_onetime_effect(id=6, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 업적_02(self.ctx)


class 업적_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=701, type='trigger', achieve='ChristmasWish')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 강제이동(self.ctx)


class 강제이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=63000075, portal_id=10)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_scene_skip() # Missing State: State


initial_state = 준비
