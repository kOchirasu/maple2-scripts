""" trigger/02000535_bf/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


# 플레이어 감지
class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2)
        self.set_effect(trigger_ids=[801])
        self.set_effect(trigger_ids=[802])
        self.set_mesh(trigger_ids=[4002], visible=True)
        self.set_mesh(trigger_ids=[4003], visible=True)
        self.set_mesh(trigger_ids=[4004], visible=True)
        self.set_mesh(trigger_ids=[4005], visible=True)
        self.set_mesh(trigger_ids=[4006], visible=True)
        self.set_mesh(trigger_ids=[4007], visible=True)
        self.set_mesh(trigger_ids=[4008], visible=True)
        self.set_mesh(trigger_ids=[4009], visible=True)
        self.set_mesh(trigger_ids=[4010], visible=True)
        self.set_mesh(trigger_ids=[4011], visible=True)
        self.set_mesh(trigger_ids=[4012], visible=True)
        self.set_mesh(trigger_ids=[4013], visible=True)
        self.set_mesh(trigger_ids=[4014], visible=True)
        self.set_mesh(trigger_ids=[4015], visible=True)
        self.set_mesh(trigger_ids=[4016], visible=True)
        self.set_mesh(trigger_ids=[4017], visible=True)
        self.set_mesh(trigger_ids=[4018], visible=True)
        self.set_mesh(trigger_ids=[4019], visible=True)
        self.set_interact_object(trigger_ids=[10003145], state=0)
        self.set_interact_object(trigger_ids=[10003146], state=0)
        self.set_interact_object(trigger_ids=[10003136], state=0)
        self.set_interact_object(trigger_ids=[10003137], state=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[701], job_code=0):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[5522,5523,5524,5525,5526,5527,5528,5529,5530])
        self.spawn_monster(spawn_ids=[9902,9903,9904,9905])
        self.spawn_monster(spawn_ids=[5500,5501,5502,5503,5504,5505,5506,5507,5508,5509,5510,5511,5512,5513,5514,5515,5516,5517,5518,5519,5520,5521])
        self.spawn_monster(spawn_ids=[506,507,508,509,510,511,512,513,519,518,517,516,515,514,670,671])
        self.spawn_monster(spawn_ids=[5532])
        self.move_npc(spawn_id=5532, patrol_name='MS2PatrolData_8000')
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[5531])
        self.add_balloon_talk(spawn_id=5531, msg='$02000535_BF__MAIN__0$', duration=3500)
        self.add_balloon_talk(spawn_id=5531, msg='$02000535_BF__MAIN__1$', duration=3500, delay_tick=3500)
        self.add_balloon_talk(spawn_id=5523, msg='$02000535_BF__MAIN__2$', duration=3500, delay_tick=4500)
        self.add_balloon_talk(spawn_id=5530, msg='$02000535_BF__MAIN__3$', duration=3500, delay_tick=1500)
        self.set_npc_emotion_loop(spawn_id=5531, sequence_name='Attack_Idle_A', duration=7000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 첫번째전투(self.ctx)


class 첫번째전투(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[5523,5524,5525,5526,5527,5528,5529,5530,5531])
        self.spawn_monster(spawn_ids=[523,524,525,526,527,528,529,530,531])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[523,524,525,526,527,528,529,530,531]):
            return 다음으로이동(self.ctx)


# 이동
class 다음으로이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10003146], state=1)
        self.destroy_monster(spawn_ids=[523,524,525,526,527,528,529,530,531])
        self.add_balloon_talk(msg='$02000535_BF__MAIN__4$', duration=3500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[706], job_code=0):
            return 너무많아(self.ctx)


class 너무많아(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10003146], state=0):
            return 머리를쓰자(self.ctx)


class 머리를쓰자(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(msg='$02000535_BF__MAIN__5$', duration=3500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 바닥을보여주자(self.ctx)


class 바닥을보여주자(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[802], visible=True)
        self.set_event_ui_script(type=BannerType.Text, script='$02000535_BF__MAIN__6$', duration=5000)
        self.set_interact_object(trigger_ids=[10003136], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10003136], state=0):
            return 타이밍맞추기1(self.ctx)


class 타이밍맞추기1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4000])
        self.set_interact_object(trigger_ids=[10003136], state=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[709], job_code=0):
            return 머리를쓰자2(self.ctx)


class 머리를쓰자2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=5532, msg='$02000535_BF__MAIN__7$', duration=3500, delay_tick=300)
        self.add_balloon_talk(spawn_id=5501, msg='$02000535_BF__MAIN__8$', duration=3500, delay_tick=800)
        self.add_balloon_talk(spawn_id=5502, msg='$02000535_BF__MAIN__9$', duration=3500, delay_tick=800)
        self.add_balloon_talk(spawn_id=5503, msg='$02000535_BF__MAIN__10$', duration=3500, delay_tick=1000)
        self.add_balloon_talk(spawn_id=5504, msg='$02000535_BF__MAIN__11$', duration=3500, delay_tick=1000)
        self.add_balloon_talk(spawn_id=5505, msg='$02000535_BF__MAIN__12$', duration=3500, delay_tick=1000)
        self.add_balloon_talk(spawn_id=5522, msg='$02000535_BF__MAIN__13$', duration=3500, delay_tick=300)
        self.add_balloon_talk(spawn_id=5520, msg='$02000535_BF__MAIN__14$', duration=3500, delay_tick=300)
        self.add_balloon_talk(spawn_id=5521, msg='$02000535_BF__MAIN__15$', duration=3500, delay_tick=1500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 통로이동1(self.ctx)


class 통로이동1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=5520, msg='$02000535_BF__MAIN__16$', duration=5500, delay_tick=4500)
        self.add_balloon_talk(spawn_id=5522, msg='$02000535_BF__MAIN__17$', duration=5500, delay_tick=7500)
        self.add_balloon_talk(spawn_id=5505, msg='$02000535_BF__MAIN__18$', duration=5500, delay_tick=8500)
        self.add_balloon_talk(spawn_id=5522, msg='$02000535_BF__MAIN__19$', duration=5500, delay_tick=12500)
        self.spawn_monster(spawn_ids=[5000,5001,5002,5003,5004])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[702], job_code=0):
            return 메이드대사(self.ctx)


class 메이드대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=670, msg='$02000535_BF__MAIN__20$', duration=3500, delay_tick=1500)
        self.add_balloon_talk(spawn_id=671, msg='$02000535_BF__MAIN__21$', duration=3500)
        self.set_npc_emotion_loop(spawn_id=670, sequence_name='Attack_Idle_A', duration=5000.0)
        self.set_npc_emotion_loop(spawn_id=671, sequence_name='Attack_Idle_A', duration=5000.0)
        self.destroy_monster(spawn_ids=[5000,5001,5002,5003,5004])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 흑성회스폰(self.ctx)


class 흑성회스폰(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[670,671])
        self.spawn_monster(spawn_ids=[601,602,603,604,605])
        self.spawn_monster(spawn_ids=[680,681])
        self.add_balloon_talk(spawn_id=604, msg='$02000535_BF__MAIN__22$', duration=3500, delay_tick=500)
        self.add_balloon_talk(spawn_id=602, msg='$02000535_BF__MAIN__23$', duration=3500, delay_tick=1500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[601,602,603,604,605,680,681]):
            return 간부들엿보기(self.ctx)


class 간부들엿보기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[705], job_code=0):
            return 간부들엿보기2(self.ctx)


class 간부들엿보기2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(msg='$02000535_BF__MAIN__24$', duration=3500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 간부들대화2(self.ctx)


class 간부들대화2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_scene_skip(state=카메라리셋시키기2, action='nextState')
        self.select_camera_path(path_ids=[2005], return_view=False)
        self.add_balloon_talk(spawn_id=9902, msg='$02000535_BF__MAIN__25$', duration=3500)
        self.add_balloon_talk(spawn_id=9903, msg='$02000535_BF__MAIN__26$', duration=3500, delay_tick=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 카메라리셋시키기2(self.ctx)


class 카메라리셋시키기2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolation_time=1.0)
        self.lock_my_pc()
        self.set_event_ui_script(type=BannerType.Text, script='$02000535_BF__MAIN__27$', duration=5000)
        self.set_effect(trigger_ids=[801], visible=True)
        self.set_interact_object(trigger_ids=[10003137], state=1)
        self.add_balloon_talk(msg='$02000535_BF__MAIN__28$', duration=3500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10003137], state=0):
            return 통로오픈(self.ctx)


class 통로오픈(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4001])
        self.side_npc_talk(npc_id=11004659, illust='BreedMin_normal', duration=4000, script='$02000535_BF__MAIN__29$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 통로오픈2(self.ctx)


class 통로오픈2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11004659, illust='BreedMin_normal', duration=4000, script='$02000535_BF__MAIN__30$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[708], job_code=0):
            return 테라스몬스터생성(self.ctx)


class 테라스몬스터생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[606,6606,608,6608])
        self.add_balloon_talk(spawn_id=606, msg='$02000535_BF__MAIN__31$', duration=5500, delay_tick=500)
        self.add_balloon_talk(spawn_id=608, msg='$02000535_BF__MAIN__32$', duration=5500, delay_tick=1500)
        self.side_npc_talk(npc_id=11004660, illust='Armand_normal', duration=4000, script='$02000535_BF__MAIN__33$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 테라스몬스터생성2(self.ctx)


class 테라스몬스터생성2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11004661, illust='Kyle_normal', duration=4000, script='$02000535_BF__MAIN__34$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[704], job_code=0):
            return 테라스몬스터생성3(self.ctx)


class 테라스몬스터생성3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[607,6607,609,610])
        self.add_balloon_talk(spawn_id=607, msg='$02000535_BF__MAIN__35$', duration=5500, delay_tick=500)
        self.add_balloon_talk(spawn_id=610, msg='$02000535_BF__MAIN__36$', duration=5500, delay_tick=2000)
        self.side_npc_talk(npc_id=11004660, illust='Armand_normal', duration=4000, script='$02000535_BF__MAIN__37$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[606,6606,608,6608,607,6607,609,610]):
            return 포탈생성(self.ctx)


class 포탈생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02000535_BF__MAIN__38$', duration=5000)
        self.set_mesh(trigger_ids=[4019])
        self.set_interact_object(trigger_ids=[10003145], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10003145], state=0):
            return 보안게임시작(self.ctx)


class 보안게임시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='GameLogicEnd', value=999)
        self.widget_action(type='Round', func='InitWidgetRound')
        self.set_user_value(trigger_id=9002, key='GameLogicStart', value=999)
        self.lock_my_pc(is_lock=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 문열기시작2(self.ctx)


class 문열기시작2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02000535_BF__MAIN__39$', duration=4000)
        self.lock_my_pc(is_lock=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            self.set_user_value(trigger_id=9002, key='GameLogicStart', value=1)
            return 게임로직종료대기(self.ctx)


class 게임로직종료대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='GameLogicEnd') == 1:
            return 게임로직종료및성공(self.ctx)
        if self.user_value(key='GameLogicEnd') == 2:
            return 게임로직종료및실패(self.ctx)


class 게임로직종료및성공(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        return 게임로직종료(self.ctx)


class 게임로직종료및실패(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        return 실패게임로직종료(self.ctx)


class 게임로직종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_loop(sequence_name='Idle_A', duration=3000.0)
        self.set_event_ui_script(type=BannerType.Text, script='$02000535_BF__MAIN__40$', duration=3000)
        self.lock_my_pc()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 이동하자(self.ctx)


class 실패게임로직종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_loop(sequence_name='Idle_A', duration=3000.0)
        self.set_event_ui_script(type=BannerType.Text, script='$02000535_BF__MAIN__41$', duration=3000)
        self.add_balloon_talk(msg='$02000535_BF__MAIN__42$', duration=3500)
        self.lock_my_pc()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 문부시기안내(self.ctx)


class 문부시기안내(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_event_ui_script(type=BannerType.Text, script='$02000535_BF__MAIN__43$', duration=5000)
        self.lock_my_pc()
        self.spawn_monster(spawn_ids=[611])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[611]):
            return 이동하자(self.ctx)


class 이동하자(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.lock_my_pc()
        self.side_npc_talk(npc_id=23300001, illust='Haren_smile', duration=4000, script='$02000535_BF__MAIN__44$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 이동하자2(self.ctx)


class 이동하자2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2, visible=True)
        self.add_balloon_talk(msg='$02000535_BF__MAIN__45$', duration=3500)


initial_state = idle
