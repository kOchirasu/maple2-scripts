""" trigger/63000073_cs/63000073_main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class 준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.spawn_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[102])
        self.spawn_monster(spawn_ids=[103])
        self.spawn_monster(spawn_ids=[104])
        self.spawn_monster(spawn_ids=[105])
        self.spawn_monster(spawn_ids=[106])
        self.spawn_monster(spawn_ids=[107])
        self.spawn_monster(spawn_ids=[108])
        self.spawn_monster(spawn_ids=[109])
        self.spawn_monster(spawn_ids=[110])
        self.spawn_monster(spawn_ids=[111])
        self.spawn_monster(spawn_ids=[112])
        self.spawn_monster(spawn_ids=[113])
        self.spawn_monster(spawn_ids=[114])
        self.spawn_monster(spawn_ids=[115])
        self.spawn_monster(spawn_ids=[116])
        self.spawn_monster(spawn_ids=[117])
        self.set_ladder(trigger_ids=[6001])
        self.set_ladder(trigger_ids=[6002])
        self.set_ladder(trigger_ids=[6003])
        self.set_ladder(trigger_ids=[6004])
        self.set_mesh(trigger_ids=[4001], visible=True)
        self.set_mesh(trigger_ids=[4002])
        self.set_portal(portal_id=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[30000372], quest_states=[3]):
            return 전투만(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[30000372], quest_states=[2]):
            return 퀘완료가능재입장(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[30000372], quest_states=[1]):
            return 잠시대기_01(self.ctx)
        if self.user_detected(box_ids=[701]):
            return 전투만(self.ctx)


class 전투만(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[115]):
            return 종료(self.ctx)

    def on_exit(self) -> None:
        self.set_ladder(trigger_ids=[6001], visible=True, enable=True)
        self.set_ladder(trigger_ids=[6002], visible=True, enable=True)
        self.set_ladder(trigger_ids=[6003], visible=True, enable=True)
        self.set_ladder(trigger_ids=[6004], visible=True, enable=True)


class 잠시대기_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.spawn_monster(spawn_ids=[121], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 잠시대기_02(self.ctx)


class 잠시대기_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8001], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 보보스퇴장_01(self.ctx)


class 보보스퇴장_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_scene_skip(state=보보스퇴장_03, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 보보스퇴장_02(self.ctx)


class 보보스퇴장_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=121, patrol_name='MS2PatrolData_2001')
        # 책 틈에서 지내게 해줬으니, 소원 들어준 거야…
        self.add_balloon_talk(spawn_id=121, msg='$63000073_CS__63000073_MAIN__0$', duration=2500, delay_tick=1000)
        # self.add_cinematic_talk(npc_id=11004371, msg='책 틈에서 지내게 했으니, 소원 들어준 거야…', duration=2000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 보보스퇴장_03(self.ctx)


class 보보스퇴장_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 보보스퇴장_04(self.ctx)

    def on_exit(self) -> None:
        self.reset_camera()
        self.destroy_monster(spawn_ids=[121])


class 보보스퇴장_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.show_guide_summary(entity_id=26300731, text_id=26300731)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[115]):
            return 사다리등장_01(self.ctx)


class 사다리등장_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=26300731)
        self.set_ladder(trigger_ids=[6001], visible=True, enable=True)
        self.set_ladder(trigger_ids=[6002], visible=True, enable=True)
        self.set_ladder(trigger_ids=[6003], visible=True, enable=True)
        self.set_ladder(trigger_ids=[6004], visible=True, enable=True)
        self.show_guide_summary(entity_id=26300733, text_id=26300733)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001385], state=0):
            return 트렁크오픈_01(self.ctx)


class 트렁크오픈_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=26300733)
        self.spawn_monster(spawn_ids=[122], auto_target=False)
        self.set_mesh(trigger_ids=[4001])
        self.set_mesh(trigger_ids=[4002], visible=True)
        self.show_guide_summary(entity_id=26300732, text_id=26300732)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[702], quest_ids=[30000372], quest_states=[2]):
            return 트렁크오픈_02(self.ctx)


class 퀘완료가능재입장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.spawn_monster(spawn_ids=[122], auto_target=False)
        self.set_mesh(trigger_ids=[4001])
        self.set_mesh(trigger_ids=[4002], visible=True)
        self.set_ladder(trigger_ids=[6001], visible=True, enable=True)
        self.set_ladder(trigger_ids=[6002], visible=True, enable=True)
        self.set_ladder(trigger_ids=[6003], visible=True, enable=True)
        self.set_ladder(trigger_ids=[6004], visible=True, enable=True)
        self.move_user(map_id=63000073, portal_id=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 트렁크오픈_02(self.ctx)


class 트렁크오픈_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.hide_guide_summary(entity_id=26300732)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 트렁크오픈_03(self.ctx)


class 트렁크오픈_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_2002')
        self.select_camera_path(path_ids=[8002], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 트렁크오픈_04(self.ctx)


class 트렁크오픈_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_scene_skip(state=에이든퇴장_01, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 에이든대화_01(self.ctx)


class 에이든대화_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8003], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=122, sequence_name='Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 에이든대화_02(self.ctx)


class 에이든대화_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004359, msg='$63000073_CS__63000073_MAIN__1$', duration=2500, align=Align.Right, illust_id='0') # 아… 머리야.\n이게 어떻게 된 일이지

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 에이든대화_03(self.ctx)


class 에이든대화_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8004], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 에이든대화_04(self.ctx)


class 에이든대화_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_loop(sequence_name='Talk_A', duration=2500.0)
        self.add_cinematic_talk(npc_id=0, msg='$63000073_CS__63000073_MAIN__2$', duration=2500, align=Align.Right) # $npcName:11004359$이지?

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 에이든대화_05(self.ctx)


class 에이든대화_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_loop(sequence_name='Talk_A', duration=2500.0)
        # 네 동생, $npcName:11004354$$pp:가,이$ 마을에서 널 기다리고 있어.\n마을에서 같이 부모님을 찾아보자고 하는데.
        self.add_cinematic_talk(npc_id=0, msg='$63000073_CS__63000073_MAIN__3$', duration=4500, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 에이든대화_06(self.ctx)


class 에이든대화_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8003], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 에이든대화_07(self.ctx)


class 에이든대화_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=122, sequence_name='Talk_A', duration=3500.0)
        # …뭐라고?\n그럼… 나만 당한 게 아닌 건가?
        self.add_cinematic_talk(npc_id=11004359, msg='$63000073_CS__63000073_MAIN__4$', duration=3500, align=Align.Right, illust_id='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 에이든대화_08(self.ctx)


class 에이든대화_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=122, sequence_name='Talk_A', duration=4500.0)
        # 어서 $npcName:11004354$$pp:를,을$ 만나봐야겠군.\n먼저 출발할게, 마을에서 보자.
        self.add_cinematic_talk(npc_id=11004359, msg='$63000073_CS__63000073_MAIN__5$', duration=4500, align=Align.Right, illust_id='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 에이든퇴장_01(self.ctx)


class 에이든퇴장_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.reset_camera()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawn_ids=[122])

    def on_tick(self) -> trigger_api.Trigger:
        return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)


initial_state = 준비
