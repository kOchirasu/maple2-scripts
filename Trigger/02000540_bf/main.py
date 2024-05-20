""" trigger/02000540_bf/main.xml """
import trigger_api
from System.Numerics import Vector3


# 플레이어 감지
class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ambient_light(primary=Vector3(132,195,255))
        self.set_directional_light(diffuse_color=Vector3(163,115,143), specular_color=Vector3(140,140,140))
        self.set_portal(portal_id=2)
        self.set_portal(portal_id=6002)
        self.set_portal(portal_id=6003)
        self.set_portal(portal_id=6004)
        self.set_portal(portal_id=6005)
        self.set_interact_object(trigger_ids=[10003138], state=0)
        self.set_interact_object(trigger_ids=[10003139], state=0)
        self.set_interact_object(trigger_ids=[10003140], state=0)
        self.set_interact_object(trigger_ids=[10003141], state=0)
        self.enable_spawn_point_pc(spawn_id=0, is_enable=True)
        self.enable_spawn_point_pc(spawn_id=1)
        self.set_effect(trigger_ids=[9000])
        self.set_effect(trigger_ids=[9001])
        self.set_effect(trigger_ids=[9002])
        self.set_effect(trigger_ids=[9003])
        self.set_effect(trigger_ids=[8000], visible=True)
        self.set_effect(trigger_ids=[8001])
        self.set_effect(trigger_ids=[8002])
        self.set_effect(trigger_ids=[8003])
        self.set_effect(trigger_ids=[8004])
        self.set_effect(trigger_ids=[8005])
        self.set_effect(trigger_ids=[8006])
        self.set_effect(trigger_ids=[8007])
        self.set_effect(trigger_ids=[8008])
        self.spawn_monster(spawn_ids=[614])
        self.set_onetime_effect(id=101, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=102, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=103, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=104, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=105, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[701], job_code=0):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2)
        self.set_effect(trigger_ids=[8000], visible=True)
        self.set_event_ui(type=1, arg2='$02000540_BF__MAIN__0$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[708], job_code=0):
            return 전투판으로이동하면(self.ctx)


class 전투판으로이동하면(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[601,6011,6012])
        self.add_balloon_talk(spawn_id=601, msg='$02000540_BF__MAIN__1$', duration=3500)
        self.add_balloon_talk(spawn_id=6011, msg='$02000540_BF__MAIN__2$', duration=3500, delay_tick=1500)
        self.side_npc_talk(npc_id=11004643, illust='SlaveWoman3_normal', duration=3000, script='$02000540_BF__MAIN__3$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[709], job_code=0):
            return 전투판으로이동하면2(self.ctx)


class 전투판으로이동하면2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[602,6021,6022,603])
        self.add_balloon_talk(spawn_id=603, msg='$02000540_BF__MAIN__4$', duration=3500, delay_tick=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[601,6011,6012,602,6021,6022,603]):
            return 첫번째오브젝트조사(self.ctx)


class 첫번째오브젝트조사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000540_BF__MAIN__5$', arg3='3000')
        self.set_interact_object(trigger_ids=[10003138], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10003138], state=0):
            return 첫번째불켰음(self.ctx)


class 첫번째불켰음(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8001], visible=True)
        self.set_onetime_effect(id=101, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_event_ui(type=1, arg2='$02000540_BF__MAIN__6$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[704], job_code=0):
            return 두번째몬스터생성(self.ctx)


class 두번째몬스터생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[9000])
        self.spawn_monster(spawn_ids=[604,6041,6042], auto_target=False)
        self.side_npc_talk(npc_id=11004643, illust='SlaveWoman3_normal', duration=3000, script='$02000540_BF__MAIN__7$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[710], job_code=0):
            return 두번째전투판으로이동하면(self.ctx)


class 두번째전투판으로이동하면(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[605,6051,6052,606])
        self.add_balloon_talk(spawn_id=606, msg='$02000540_BF__MAIN__8$', duration=3500, delay_tick=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[604,6041,6042,605,6051,6052,606]):
            return 두번째오브젝트조사(self.ctx)


class 두번째오브젝트조사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000540_BF__MAIN__9$', arg3='3000')
        self.set_interact_object(trigger_ids=[10003139], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10003139], state=0):
            return 세번째전투판체크(self.ctx)


class 세번째전투판체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8002], visible=True)
        self.set_onetime_effect(id=102, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_event_ui(type=1, arg2='$02000540_BF__MAIN__10$', arg3='3000')
        self.set_effect(trigger_ids=[8005], visible=True)
        self.set_effect(trigger_ids=[8006], visible=True)
        self.set_portal(portal_id=6002, visible=True)
        self.set_portal(portal_id=6003, visible=True)
        self.add_balloon_talk(spawn_id=614, msg='$02000540_BF__MAIN__11$', duration=6500, delay_tick=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[705], job_code=0):
            return 세번째몬스터생성(self.ctx)


class 세번째몬스터생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[9001])
        self.spawn_monster(spawn_ids=[607,6071,6072], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[711], job_code=0):
            return 세번째전투판으로이동하면(self.ctx)


class 세번째전투판으로이동하면(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[608,6081,6082,609])
        self.add_balloon_talk(spawn_id=609, msg='$02000540_BF__MAIN__12$', duration=3500, delay_tick=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[607,6071,6072,608,6081,6082,609]):
            return 세번째오브젝트조사(self.ctx)


class 세번째오브젝트조사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000540_BF__MAIN__13$', arg3='3000')
        self.set_interact_object(trigger_ids=[10003140], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10003140], state=0):
            return 네번째전투판체크(self.ctx)


class 네번째전투판체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8003], visible=True)
        self.set_onetime_effect(id=103, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_event_ui(type=1, arg2='$02000540_BF__MAIN__14$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[706], job_code=0):
            return 네번째몬스터생성(self.ctx)


class 네번째몬스터생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[9002])
        self.spawn_monster(spawn_ids=[610,6101,6102], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[712], job_code=0):
            return 네번째전투판으로이동하면(self.ctx)


class 네번째전투판으로이동하면(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[611,6111,6112,612])
        self.add_balloon_talk(spawn_id=612, msg='$02000540_BF__MAIN__15$', duration=3500, delay_tick=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[610,6101,6102,611,6111,6112,612]):
            return 네번째오브젝트조사(self.ctx)


class 네번째오브젝트조사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000540_BF__MAIN__16$', arg3='3000')
        self.set_interact_object(trigger_ids=[10003141], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10003141], state=0):
            return 보스전투판완성시키기(self.ctx)


class 보스전투판완성시키기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8004], visible=True)
        self.set_onetime_effect(id=104, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_event_ui(type=1, arg2='$02000540_BF__MAIN__17$', arg3='3000')
        self.set_ambient_light(primary=Vector3(237,225,255))
        self.set_directional_light(diffuse_color=Vector3(232,212,127), specular_color=Vector3(140,140,140))
        self.set_portal(portal_id=6004, visible=True)
        self.set_portal(portal_id=6005, visible=True)
        self.set_effect(trigger_ids=[8007], visible=True)
        self.set_effect(trigger_ids=[8008], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 보스등장전에(self.ctx)


class 보스등장전에(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11004643, illust='SlaveWoman3_normal', duration=3000, script='$02000540_BF__MAIN__18$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[707], job_code=0):
            return 보스등장(self.ctx)


class 보스등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[9003])
        self.enable_spawn_point_pc(spawn_id=0)
        self.enable_spawn_point_pc(spawn_id=1, is_enable=True)
        self.set_onetime_effect(id=105, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.side_npc_talk(npc_id=11004643, illust='SlaveWoman3_normal', duration=3000, script='$02000540_BF__MAIN__19$')
        self.spawn_monster(spawn_ids=[613])
        self.set_portal(portal_id=6005)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[613]):
            return 다리생성(self.ctx)


class 다리생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11004643, illust='SlaveWoman3_normal', duration=3000, script='$02000540_BF__MAIN__20$')
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)


initial_state = idle
