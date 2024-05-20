""" trigger/52020006_qd/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,102,103,104])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return 퀘스트조건체크(self.ctx)


class 퀘스트조건체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001797], quest_states=[3]):
            return 빈방(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001797], quest_states=[2]):
            return 빈방(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001797], quest_states=[1]):
            return 제이든_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001796], quest_states=[3]):
            return 제이든_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001796], quest_states=[2]):
            return 제이든_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001796], quest_states=[1]):
            return 세리하와함께전투_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001795], quest_states=[3]):
            return 세리하_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001795], quest_states=[2]):
            return 세리하_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001795], quest_states=[1]):
            return 세리하와아르망_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001794], quest_states=[3]):
            return 세리하_대기(self.ctx)


class 세리하_대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,102,105])
        self.spawn_monster(spawn_ids=[101], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001796], quest_states=[1]):
            return 세리하와함께전투_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001795], quest_states=[1]):
            return 세리하와아르망_대기(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return 조건확인_대기01(self.ctx)


class 제이든_대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,102,105])
        self.spawn_monster(spawn_ids=[105], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001796], quest_states=[1]):
            return 세리하와함께전투_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001795], quest_states=[1]):
            return 세리하와아르망_대기(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return 조건확인_대기01(self.ctx)


class 빈방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,102,105])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001796], quest_states=[1]):
            return 세리하와함께전투_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001795], quest_states=[1]):
            return 세리하와아르망_대기(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class 조건확인_대기01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001796], quest_states=[1]):
            return 세리하와함께전투_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001795], quest_states=[1]):
            return 세리하와아르망_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001795], quest_states=[3]):
            return 조건확인_대기02(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001795], quest_states=[2]):
            return 조건확인_대기02(self.ctx)
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[50001796], quest_states=[1]):
            return 조건확인_대기02(self.ctx)
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[50001795], quest_states=[1]):
            return 조건확인_대기02(self.ctx)


class 조건확인_대기02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001796], quest_states=[1]):
            return 세리하와함께전투_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001795], quest_states=[1]):
            return 세리하와아르망_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001795], quest_states=[3]):
            return 조건확인_대기01(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001795], quest_states=[2]):
            return 조건확인_대기01(self.ctx)
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[50001796], quest_states=[1]):
            return 조건확인_대기01(self.ctx)
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[50001795], quest_states=[1]):
            return 조건확인_대기01(self.ctx)


class 세리하와아르망_대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,102,105])
        self.spawn_monster(spawn_ids=[101,102], auto_target=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[50001795], quest_states=[1]):
            return 퀘스트조건체크(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return 세리하와아르망_준비(self.ctx)


class 세리하와아르망_준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.select_camera_path(path_ids=[8000], return_view=False)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.visible_my_pc(is_visible=False) # PC안보이게

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 세리하와아르망_연출시작(self.ctx)


class 세리하와아르망_연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip(state=세리하와아르망_스킵완료, action='exit') # setsceneskip 1 set
        # setsceneskip 1 set
        # setsceneskip 1 set

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 세리하와아르망_연출01(self.ctx)


class 세리하와아르망_연출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8000], return_view=False)
        self.add_cinematic_talk(npc_id=11003548, illust_id='Seriha_normal', msg='연출 보강 예정', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 세리하와아르망_연출02(self.ctx)


class 세리하와아르망_연출02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8000], return_view=False)
        self.add_cinematic_talk(npc_id=11003658, illust_id='Armand_normal', msg='조금만 기다려 주세요', duration=3000)
        self.visible_my_pc(is_visible=True) # PC보이게

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 세리하와아르망_연출03(self.ctx)


class 세리하와아르망_연출03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8000], return_view=False)
        self.add_cinematic_talk(npc_id=11003548, illust_id='Seriha_normal', msg='죄송합니다', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 세리하와아르망_마무리(self.ctx)


class 세리하와아르망_마무리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[102])
        # Missing State: State,  setsceneskip 1 close
        self.set_scene_skip()
        # setsceneskip 1 close
        # setsceneskip 1 close
        # setsceneskip 1 close

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 세리하와아르망_연출종료(self.ctx)


class 세리하와아르망_스킵완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,102,105])
        self.spawn_monster(spawn_ids=[101])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 세리하와아르망_연출종료(self.ctx)


class 세리하와아르망_연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=2.0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_achievement(trigger_id=9000, type='trigger', achieve='Armandsidentity')
        self.visible_my_pc(is_visible=True) # PC보이게
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 조건확인_대기01(self.ctx)


class 세리하와함께전투_대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,102,105])
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[50001796], quest_states=[1]):
            return 퀘스트조건체크(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return 세리하와함께전투_준비(self.ctx)


class 세리하와함께전투_준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[150,151,152,153])
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 세리하와함께전투_연출시작(self.ctx)


class 세리하와함께전투_연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip(state=세리하와함께전투_전투직전스킵, action='exit') # setsceneskip 2 set
        # setsceneskip 2 set
        # setsceneskip 2 set

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 세리하와함께전투_연출01(self.ctx)


class 세리하와함께전투_연출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8000], return_view=False)
        self.add_cinematic_talk(npc_id=11003548, illust_id='Seriha_normal', msg='그럼 누가 먼저 저것들을 쓸어버리나 내기하자고.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 세리하와함께전투_연출02(self.ctx)


class 세리하와함께전투_연출02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8002], return_view=False)
        self.add_cinematic_talk(npc_id=0, msg='임시연출이라 몬스터가 허약할 거야.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 세리하와함께전투_연출03(self.ctx)


class 세리하와함께전투_연출03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[111], auto_target=False)
        self.select_camera_path(path_ids=[8010], return_view=False)
        self.add_cinematic_talk(npc_id=29000335, illust_id='Seriha_normal', msg='간다!', duration=3000)
        # Missing State: State,  setsceneskip 2 close
        self.set_scene_skip()
        # setsceneskip 2 close
        # setsceneskip 2 close
        # setsceneskip 2 close

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 전투대기01(self.ctx)


class 세리하와함께전투_전투직전스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,102,105])
        self.spawn_monster(spawn_ids=[101])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 전투대기01(self.ctx)


class 전투대기01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=2.0)
        # self.add_cinematic_talk(npc_id=29000251, illust_id='11000015', msg='$52000121_QD__MAIN__17$', duration=2000, align=Align.Left)
        # self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 전투준비01(self.ctx)


class 전투준비01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[150,151,152,153]):
            return 전투끝(self.ctx)


class 전투끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8040], return_view=False)
        # self.set_achievement(trigger_id=9000, type='trigger', achieve='FightingSeriha')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 암전02(self.ctx)


class 암전02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return npc교체01(self.ctx)


class npc교체01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[111])
        self.spawn_monster(spawn_ids=[110], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 전투후제이든등장_연출준비(self.ctx)


class 전투후제이든등장_연출준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[111])
        self.spawn_monster(spawn_ids=[110], auto_target=False)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(path_ids=[8020], return_view=False)
        self.set_scene_skip(state=전투후제이든등장_스킵완료, action='exit') # setsceneskip 3 set
        # setsceneskip 3 set
        # setsceneskip 3 set

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 전투후제이든등장_01_세리하소멸(self.ctx)


class 전투후제이든등장_01_세리하소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_Armand_comingout')
        # self.move_user_path(patrol_name='MS2PatrolData_PC_Surprised')
        self.add_cinematic_talk(npc_id=11003548, illust_id='Seriha_normal', msg='내가 이긴 듯. 그럼 이만!', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 전투후제이든등장_02_PC독백(self.ctx)


class 전투후제이든등장_02_PC독백(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[110])
        self.add_cinematic_talk(npc_id=0, illust_id='Seriha_normal', msg='이제 저 너머로 갈 차례인가...', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 전투후제이든등장_03_제이든등장(self.ctx)


class 전투후제이든등장_03_제이든등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[105], auto_target=False)
        self.add_cinematic_talk(npc_id=11003677, illust_id='Jaiden_normal', msg='무사했구나, $MyPCName$.', duration=3000)
        # Missing State: State,  setsceneskip 3 close
        self.set_scene_skip()
        # setsceneskip 3 close
        # setsceneskip 3 close
        # setsceneskip 3 close

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 세리하와함께전투_제이든등장_연출종료(self.ctx)


class 전투후제이든등장_스킵완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,102,105,110,111,150,151,152,153])
        self.spawn_monster(spawn_ids=[105])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return None # Missing State: 세리하와함께전투_연출종료


class 세리하와함께전투_제이든등장_연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=2.0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_achievement(trigger_id=9000, type='trigger', achieve='FightingSeriha')
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=2.0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
