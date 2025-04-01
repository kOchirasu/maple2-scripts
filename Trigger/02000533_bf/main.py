""" trigger/02000533_bf/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


# 플레이어 감지
class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[901], visible=True)
        self.set_mesh(trigger_ids=[3000,3001,3002,3003], visible=True)
        self.set_interact_object(trigger_ids=[10003144], state=0)
        self.set_portal(portal_id=2)
        self.set_effect(trigger_ids=[7000])
        self.spawn_monster(spawn_ids=[603,604,605,606])
        self.move_npc(spawn_id=603, patrol_name='MS2PatrolData_5003')
        self.move_npc(spawn_id=604, patrol_name='MS2PatrolData_5004')
        self.move_npc(spawn_id=605, patrol_name='MS2PatrolData_5005')
        self.move_npc(spawn_id=606, patrol_name='MS2PatrolData_5006')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[701], job_code=0):
            return 출입문부시기(self.ctx)


class 출입문부시기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2)
        self.side_npc_talk(npc_id=11004639, illust='Jay_normal', duration=3000, script='$02000533_BF__MAIN__0$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 출입문부시기2(self.ctx)


class 출입문부시기2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02000533_BF__MAIN__1$', duration=3000)
        self.spawn_monster(spawn_ids=[508])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[508]):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7000], visible=True)
        self.set_mesh(trigger_ids=[3000,3001,3002,3003])
        self.spawn_monster(spawn_ids=[501,502])
        self.add_balloon_talk(spawn_id=501, msg='$02000533_BF__MAIN__2$', duration=3500)
        self.side_npc_talk(npc_id=21450001, illust='Mafia1_normal', duration=4000, script='$02000533_BF__MAIN__3$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[704], job_code=0):
            return 층으로22_3(self.ctx)


class 층으로22_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[503,5503])
        self.side_npc_talk(npc_id=11004639, illust='Jay_normal', duration=4000, script='$02000533_BF__MAIN__4$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 층으로3_3(self.ctx)


class 층으로3_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[504,5504,505,506,509])
        self.add_balloon_talk(spawn_id=5504, msg='$02000533_BF__MAIN__5$', duration=3500, delay_tick=2000)
        self.add_balloon_talk(spawn_id=505, msg='$02000533_BF__MAIN__6$', duration=3500, delay_tick=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[501,502,503,504,5503,5504,505,506,509]):
            return 다죽이면(self.ctx)


class 다죽이면(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10003144], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10003144], state=0):
            return 문열기시도(self.ctx)


class 문열기시도(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 문열기게임(self.ctx)


class 문열기게임(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.side_npc_talk(npc_id=11004639, illust='Jay_normal', duration=4000, script='$02000533_BF__MAIN__7$')
        self.set_user_value(key='GameLogicEnd', value=999)
        self.widget_action(type='Round', func='InitWidgetRound')
        self.set_user_value(trigger_id=9002, key='GameLogicStart', value=999)
        self.lock_my_pc(is_lock=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 문열기시작2(self.ctx)


class 문열기시작2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02000533_BF__MAIN__8$', duration=4000)
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
        self.set_event_ui_script(type=BannerType.Text, script='$02000533_BF__MAIN__9$', duration=3000)
        self.lock_my_pc()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 이동하자(self.ctx)


class 실패게임로직종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02000533_BF__MAIN__10$', duration=3000)
        self.lock_my_pc()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 문손으로부시기(self.ctx)


class 문손으로부시기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.lock_my_pc()
        self.add_cinematic_talk(npc_id=0, msg='$02000533_BF__MAIN__11$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 문부시기안내(self.ctx)


class 문부시기안내(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_event_ui_script(type=BannerType.Text, script='$02000533_BF__MAIN__12$', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[507]):
            return 문을부시고이동(self.ctx)


class 문을부시고이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11004639, illust='Jay_normal', duration=4000, script='$02000533_BF__MAIN__13$')
        self.spawn_monster(spawn_ids=[507])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[507]):
            return 문을부시고이동2(self.ctx)


class 문을부시고이동2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[901], start_delay=1)
        self.set_portal(portal_id=2, visible=True)
        self.lock_my_pc()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 이동하자(self.ctx)


class 이동하자(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11004639, illust='Jay_normal', duration=4000, script='$02000533_BF__MAIN__14$')
        self.set_mesh(trigger_ids=[901], start_delay=1)
        self.set_portal(portal_id=2, visible=True)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.lock_my_pc()


initial_state = idle
