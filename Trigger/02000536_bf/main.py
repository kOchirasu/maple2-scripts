""" trigger/02000536_bf/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


# 플레이어 감지
class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2)
        self.spawn_monster(spawn_ids=[501,502,504,505,506,507,508,509,510,511], auto_target=False)
        self.set_interact_object(trigger_ids=[10003147], state=0)
        self.set_mesh(trigger_ids=[9999], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[701], job_code=0):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_scene_skip() # Missing State: State
        self.spawn_monster(spawn_ids=[102], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return start(self.ctx)


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=전투시작, action='nextState')
        self.select_camera_path(path_ids=[7000,7003], return_view=False)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.show_caption(type='VerticalCaption', title='$02000536_BF__MAIN__0$', desc='$02000536_BF__MAIN__1$', align=Align.Center | Align.Right, duration=3000, scale=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 하렌인사(self.ctx)


class 하렌인사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[7003,7001], return_view=False)
        self.set_npc_emotion_loop(spawn_id=102, sequence_name='Bore_A', duration=5000.0)
        self.add_cinematic_talk(npc_id=23300001, msg='$02000536_BF__MAIN__2$', align=Align.Center, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4500):
            return 하렌인사2(self.ctx)


class 하렌인사2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=102, sequence_name='Attack_01_E,Attack_01_B')
        self.add_cinematic_talk(npc_id=23300001, msg='$02000536_BF__MAIN__3$', align=Align.Center, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 전투시작(self.ctx)


class 전투시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolation_time=1.0)
        self.set_event_ui(type=1, arg2='$02000536_BF__MAIN__4$', arg3='3000')
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.destroy_monster(spawn_ids=[102])

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_hp(spawn_id=101, is_relative=True) <= 70:
            return 메이드군단을스폰(self.ctx)


class 메이드군단을스폰(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[301,302,303,304], auto_target=False)
        self.side_npc_talk(npc_id=23300001, illust='Haren_serious', duration=4000, script='$02000536_BF__MAIN__5$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_hp(spawn_id=101, is_relative=True) <= 50:
            return 메이드군단을스폰2(self.ctx)


class 메이드군단을스폰2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[401,402,403,404], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_hp(spawn_id=101, is_relative=True) <= 30:
            return 몬스터사망체크(self.ctx)


class 몬스터사망체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=23300001, illust='Haren_serious', duration=4000, script='$02000536_BF__MAIN__6$')
        self.spawn_monster(spawn_ids=[201,202,203,204], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101]):
            return 던전클리어(self.ctx)


"""
class 금고찾기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000536_BF__MAIN__7$', arg3='3000')
        self.set_interact_object(trigger_ids=[10003147], state=1)
        self.destroy_monster(spawn_ids=[201,202,203,204,301,302,303,304,401,402,403,404])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10003147], state=0):
            return 던전클리어(self.ctx)
"""

class 던전클리어(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=23300001, illust='Haren_serious', duration=3000, script='$02000536_BF__MAIN__8$')
        self.set_mesh(trigger_ids=[9999])
        self.destroy_monster(spawn_ids=[-1])
        self.dungeon_clear() # 보스 잡히고 던전 클리어 선언 먼저

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 트리거완료(self.ctx)


class 트리거완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.dungeon_clear()
        # 보스가 순삭 될 경우 트리거 타이밍이 어긋나서 소환몹 제거 안될 수 있기 때문에 혹시 몰라 최종 마지막에 몬스터 제거 명령 설정함
        self.destroy_monster(spawn_ids=[-1])
        # 보스가 순삭될 경우 던전 클리어 선언되기 전에 포털로 나갈 우려가 있으므로 포털 오픈은 던전 클리어 이후 시점으로
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)


initial_state = idle
