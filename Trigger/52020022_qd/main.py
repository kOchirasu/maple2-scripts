""" trigger/52020022_qd/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,102,103,104,111,115])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return 퀘스트조건체크(self.ctx)


class 퀘스트조건체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001791], quest_states=[3]):
            return 빈방(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001791], quest_states=[2]):
            return 기본_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001791], quest_states=[1]):
            return 기본_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001790], quest_states=[3]):
            return 기본_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001790], quest_states=[2]):
            return 기본_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001790], quest_states=[1]):
            return 기본_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001784], quest_states=[3]):
            return 기본_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001784], quest_states=[2]):
            return 세리하_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001784], quest_states=[1]):
            return 기본_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001783], quest_states=[3]):
            return 기본_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001783], quest_states=[2]):
            return 기본_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001783], quest_states=[1]):
            return 기본_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001782], quest_states=[3]):
            return 기본_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001782], quest_states=[2]):
            return 기본_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001782], quest_states=[1]):
            return 기본_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001781], quest_states=[3]):
            return 기본_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001781], quest_states=[2]):
            return 기본_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001781], quest_states=[1]):
            return 기본_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001780], quest_states=[3]):
            return 기본_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001780], quest_states=[2]):
            return 아르망_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001780], quest_states=[1]):
            return 레지스탕스_대기(self.ctx)


class 기본(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 종료(self.ctx)


class 기본_대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[111], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001791], quest_states=[3]):
            return 빈방(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001784], quest_states=[2]):
            return 세리하_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001780], quest_states=[2]):
            return 아르망_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001780], quest_states=[1]):
            return 레지스탕스_대기(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class 레지스탕스_대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[102,103,104], auto_target=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[50001780], quest_states=[1]):
            return 퀘스트조건체크(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return 레지스탕스_준비(self.ctx)


class 레지스탕스_준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8000,8001], return_view=False)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 레지스탕스_연출시작(self.ctx)


class 레지스탕스_연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip(state=레지스탕스_스킵완료, action='exit') # setsceneskip 1 set
        # setsceneskip 1 set
        # setsceneskip 1 set
        self.move_user_path(patrol_name='MS2PatrolData_PC_Walkin')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 레지스탕스_체키01(self.ctx)


class 레지스탕스_체키01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8002], return_view=False)
        self.add_cinematic_talk(npc_id=11003661, illust_id='Checky_normal', msg='여기 뭐가 있긴 있는 거야?', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 레지스탕스_헨리테01(self.ctx)


class 레지스탕스_헨리테01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8003], return_view=False)
        self.add_cinematic_talk(npc_id=11003662, illust_id='henritte_normal', msg='여기 뭔가 있다는 소문도 사실은 거짓 정보 아니야?', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 레지스탕스_지그문트01(self.ctx)


class 레지스탕스_지그문트01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8004], return_view=False)
        self.add_cinematic_talk(npc_id=11003663, illust_id='sigmund_normal', msg='아니야. 연출이 있는 건 사실이지만 보강 예정이라고.\\n1월 마감 이전에 업데이트한대.', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 레지스탕스_이동(self.ctx)


class 레지스탕스_이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8006], return_view=False)
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_Goingout_Checky')
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_Goingout_Henritte')
        self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_Goingout_Sigmund')
        self.add_cinematic_talk(npc_id=11003663, illust_id='sigmund_normal', msg='그럼, 조금만 기다려 주시길...', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 레지스탕스_마무리(self.ctx)


class 레지스탕스_마무리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[102,103,104])
        # self.spawn_monster(spawn_ids=[101])
        # Missing State: State,  setsceneskip 1 close
        self.set_scene_skip()
        # setsceneskip 1 close
        # setsceneskip 1 close
        # setsceneskip 1 close

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 레지스탕스_연출종료(self.ctx)


class 레지스탕스_스킵완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,102,103,104])
        self.spawn_monster(spawn_ids=[101])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 레지스탕스_연출종료(self.ctx)


class 레지스탕스_연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=2.0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 조건확인_대기01(self.ctx)


class 조건확인_대기01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001780], quest_states=[2]):
            return 아르망_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001780], quest_states=[1]):
            return 조건확인_대기02(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001763], quest_states=[3]):
            return 조건확인_대기02(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001763], quest_states=[2]):
            return 조건확인_대기02(self.ctx)
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[50001780], quest_states=[2]):
            return 조건확인_대기02(self.ctx)


class 조건확인_대기02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001780], quest_states=[2]):
            return 아르망_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001780], quest_states=[1]):
            return 조건확인_대기01(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001763], quest_states=[3]):
            return 조건확인_대기01(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001763], quest_states=[2]):
            return 조건확인_대기01(self.ctx)
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[50001780], quest_states=[2]):
            return 조건확인_대기01(self.ctx)


class 아르망_대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101], arg2=False)
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[50001780], quest_states=[2]):
            return 퀘스트조건체크(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return 아르망_준비(self.ctx)


class 아르망_준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8010], return_view=False)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 아르망_연출시작(self.ctx)


class 아르망_연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip(state=아르망_스킵완료, action='exit') # setsceneskip 2 set
        # setsceneskip 2 set
        # setsceneskip 2 set

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 아르망_연출01(self.ctx)


class 아르망_연출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8010,8011], return_view=False)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_Armand_comingout')
        self.move_user_path(patrol_name='MS2PatrolData_PC_Surprised')
        self.add_cinematic_talk(npc_id=11003672, illust_id='Armand_normal', msg='연출 추가 예정입니다.', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 아르망_마무리(self.ctx)


class 아르망_마무리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,111])
        self.spawn_monster(spawn_ids=[111])
        # Missing State: State,  setsceneskip 2 close
        self.set_scene_skip()
        # setsceneskip 2 close
        # setsceneskip 2 close
        # setsceneskip 2 close

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 연출종료(self.ctx)


class 아르망_스킵완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,111])
        self.spawn_monster(spawn_ids=[111])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출종료(self.ctx)


class 세리하_대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[111,115], auto_target=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[50001784], quest_states=[2]):
            return 퀘스트조건체크(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return 세리하_준비(self.ctx)


class 세리하_준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8014], return_view=False)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.visible_my_pc(is_visible=False) # PC안보이게

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 세리하_연출시작(self.ctx)


class 세리하_연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip(state=세리하_스킵완료, action='exit') # setsceneskip 3 set
        # setsceneskip 3 set
        # setsceneskip 3 set

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 세리하_연출01(self.ctx)


class 세리하_연출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8021], return_view=False)
        self.add_cinematic_talk(npc_id=11003660, illust_id='Seriha_normal', msg='1월 중 연출 보강 예정', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 세리하_연출02(self.ctx)


class 세리하_연출02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8014], return_view=False)
        self.add_cinematic_talk(npc_id=11003672, illust_id='Armand_normal', msg='대사 위주 보강 예정', duration=4000)
        self.visible_my_pc(is_visible=True) # PC보이게

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 세리하_마무리(self.ctx)


class 세리하_마무리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[115])
        # Missing State: State,  setsceneskip 3 close
        self.set_scene_skip()
        # setsceneskip 3 close
        # setsceneskip 3 close
        # setsceneskip 3 close

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 연출종료(self.ctx)


class 세리하_스킵완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[115])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출종료(self.ctx)


class 빈방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,102,103,104,111,115], arg2=False)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[50001791], quest_states=[3]):
            return 퀘스트조건체크(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


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
