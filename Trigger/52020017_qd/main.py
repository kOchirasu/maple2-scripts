""" trigger/52020017_qd/main.xml """
import trigger_api
from System.Numerics import Vector3
from Maple2.Server.Game.Scripting.Trigger import Align


class Idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001])
        self.set_effect(trigger_ids=[5002])
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60200115], quest_states=[1]):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[201])
        self.spawn_monster(spawn_ids=[202])
        self.spawn_monster(spawn_ids=[203])
        self.spawn_monster(spawn_ids=[204])
        self.spawn_monster(spawn_ids=[205])
        self.spawn_monster(spawn_ids=[206])
        self.spawn_monster(spawn_ids=[207])
        self.spawn_monster(spawn_ids=[208])
        self.spawn_monster(spawn_ids=[209])
        self.spawn_monster(spawn_ids=[210])
        self.spawn_monster(spawn_ids=[211])
        self.spawn_monster(spawn_ids=[212])
        self.spawn_monster(spawn_ids=[213])
        self.spawn_monster(spawn_ids=[214])
        self.spawn_monster(spawn_ids=[215])
        self.spawn_monster(spawn_ids=[216])
        self.spawn_monster(spawn_ids=[217])
        self.spawn_monster(spawn_ids=[218])
        self.spawn_monster(spawn_ids=[219])
        self.spawn_monster(spawn_ids=[220])
        self.spawn_monster(spawn_ids=[301])
        self.spawn_monster(spawn_ids=[302])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2002], quest_ids=[60200115], quest_states=[1]):
            return Object_Off(self.ctx)


class Object_Off(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ambient_light(primary=Vector3(0,0,0))
        self.spawn_monster(spawn_ids=[101]) # 엘레나
        self.set_effect(trigger_ids=[5001], visible=True)
        self.set_interact_object(trigger_ids=[10001282], state=0)
        self.add_balloon_talk(msg='!', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return Event_Start(self.ctx)


class Event_Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npc_id=11003624, msg='아아…. 드디어 극의 주인공을 찾은 것 같네.', duration=2800, align=Align.Left)
        self.set_scene_skip(action='nextState') # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Event_A_01(self.ctx)


class Event_A_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4001], return_view=False)
        self.add_cinematic_talk(npc_id=0, msg='!?', duration=1800, illust_id='0', align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Event_A_02(self.ctx)


class Event_A_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4002,4003], return_view=False)
        self.add_cinematic_talk(npc_id=11003624, msg='그래. 바로 너. 네가 주인공이야.', duration=2800, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Event_A_03(self.ctx)


class Event_A_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_3001')
        self.add_cinematic_talk(npc_id=11003624, msg='참, 주인공 역할을 말해주지 않았구나.', duration=2800, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Event_A_04(self.ctx)


class Event_A_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003624, msg='이 극의 주인공 역할은 말이야.', duration=1800, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Event_A_05(self.ctx)


class Event_A_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5002], visible=True)
        self.select_camera_path(path_ids=[4004], return_view=False)
        self.add_cinematic_talk(npc_id=11003624, msg='여기서 죽는 거야.', duration=2800, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Event_A_06(self.ctx)


class Event_A_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=2.0)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npc_id=11003624, msg='자, 그럼 극을 시작해볼까?', duration=2800, illust_id='RobotMaidBrownHair_normal', align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Event_A_End(self.ctx)


class Event_A_Skip_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101]) # 엘레나

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Event_A_Skip_02(self.ctx)


class Event_A_Skip_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_3001')
        self.set_effect(trigger_ids=[5002], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Event_A_End(self.ctx)


class Event_A_End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_ambient_light(primary=Vector3(1,1,1))
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_balloon_talk(msg='!', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Battle_A_Ready(self.ctx)


class Battle_A_Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Battle_A(self.ctx)


class Battle_A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.change_monster(from_spawn_id=201, to_spawn_id=601)
        self.change_monster(from_spawn_id=202, to_spawn_id=602)
        self.change_monster(from_spawn_id=203, to_spawn_id=603)
        self.change_monster(from_spawn_id=204, to_spawn_id=604)
        self.change_monster(from_spawn_id=205, to_spawn_id=605)
        self.change_monster(from_spawn_id=206, to_spawn_id=606)
        self.change_monster(from_spawn_id=207, to_spawn_id=607)
        self.change_monster(from_spawn_id=208, to_spawn_id=608)
        self.change_monster(from_spawn_id=209, to_spawn_id=609)
        self.change_monster(from_spawn_id=210, to_spawn_id=610)
        self.change_monster(from_spawn_id=211, to_spawn_id=611)
        self.change_monster(from_spawn_id=212, to_spawn_id=612)
        self.change_monster(from_spawn_id=213, to_spawn_id=613)
        self.change_monster(from_spawn_id=214, to_spawn_id=614)
        self.change_monster(from_spawn_id=215, to_spawn_id=615)
        self.change_monster(from_spawn_id=216, to_spawn_id=616)
        self.change_monster(from_spawn_id=217, to_spawn_id=617)
        self.change_monster(from_spawn_id=218, to_spawn_id=618)
        self.change_monster(from_spawn_id=219, to_spawn_id=619)
        self.change_monster(from_spawn_id=220, to_spawn_id=620)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620]):
            return Battle_B_Ready(self.ctx)


class Battle_B_Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Battle_B(self.ctx)


class Battle_B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.change_monster(from_spawn_id=301, to_spawn_id=701)
        self.change_monster(from_spawn_id=302, to_spawn_id=702)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[701,702]):
            return Battle_End(self.ctx)


class Battle_End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ambient_light(primary=Vector3(1,1,1))
        self.set_effect(trigger_ids=[5001])
        self.set_effect(trigger_ids=[5002])
        self.destroy_monster(spawn_ids=[101])
        self.set_interact_object(trigger_ids=[10001282], state=1)


initial_state = Idle
