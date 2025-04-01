""" trigger/02000543_bf/main.xml """
import trigger_api
from System.Numerics import Vector3
from Maple2.Server.Game.Scripting.Trigger import BannerType


# 플레이어 감지
class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ambient_light(primary=Vector3(17,196,181))
        self.set_mesh(trigger_ids=[5000,5001], visible=True)
        self.set_portal(portal_id=2)
        self.enable_spawn_point_pc(spawn_id=0, is_enable=True)
        self.enable_spawn_point_pc(spawn_id=1)
        self.set_effect(trigger_ids=[3000])
        self.set_effect(trigger_ids=[3002])
        self.set_effect(trigger_ids=[3001])
        self.set_effect(trigger_ids=[3003])
        self.set_effect(trigger_ids=[3004])
        self.set_effect(trigger_ids=[3005])
        self.set_skill(trigger_ids=[4000])
        self.set_skill(trigger_ids=[4001])
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=101, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=102, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=103, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=104, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=105, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=106, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[703], job_code=0):
            return 뒤큐브날리기전(self.ctx)


class 뒤큐브날리기전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[4000], enable=True)
        self.spawn_monster(spawn_ids=[104,105,110], auto_target=False)
        self.set_onetime_effect(id=101, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 뒤큐브날리기(self.ctx)


class 뒤큐브날리기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[3001], visible=True)
        self.side_npc_talk(npc_id=11004644, illust='SlaveMan3_normal', duration=3000, script='$02000543_BF__MAIN__0$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[701], job_code=0):
            return 게임안내(self.ctx)


class 게임안내(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[7000], return_view=False)
        self.side_npc_talk(npc_id=11004644, illust='SlaveMan3_normal', duration=3000, script='$02000543_BF__MAIN__1$')
        self.lock_my_pc(is_lock=True)
        self.set_mesh(trigger_ids=[5000,5001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 게임안내2(self.ctx)


class 게임안내2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[7000])
        self.lock_my_pc()
        self.add_balloon_talk(spawn_id=104, msg='$02000543_BF__MAIN__2$', duration=3500)
        self.add_balloon_talk(spawn_id=105, msg='$02000543_BF__MAIN__3$', duration=3500, delay_tick=500)
        self.spawn_monster(spawn_ids=[107])
        self.spawn_monster(spawn_ids=[111], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 카메라리셋(self.ctx)


class 카메라리셋(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=1.0)
        self.spawn_monster(spawn_ids=[106])
        self.spawn_monster(spawn_ids=[112], auto_target=False)
        self.side_npc_talk(npc_id=11004644, illust='SlaveMan3_normal', duration=4000, script='$02000543_BF__MAIN__4$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 게임설정(self.ctx)


class 게임설정(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=21450036, illust='DesertDragonMagicGreen_normal', duration=4000, script='$02000543_BF__MAIN__5$')
        self.set_onetime_effect(id=101, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_effect(trigger_ids=[3002], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 조건체크몬스터스폰1(self.ctx)


class 조건체크몬스터스폰1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[110])
        self.set_event_ui_script(type=BannerType.Text, script='$02000543_BF__MAIN__6$', duration=3000)
        self.set_onetime_effect(id=104, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='main') == 4:
            return 조건체크몬스터스폰2(self.ctx)


class 조건체크몬스터스폰2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return 조건체크몬스터스폰3(self.ctx)


class 조건체크몬스터스폰3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[108])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[108]):
            return 단계가기전1_2(self.ctx)


class 단계가기전1_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 단계가기전2_2(self.ctx)


class 단계가기전2_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02000543_BF__MAIN__7$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_ai_extra_data(key='phaseSecond', value=1)
            return 단계2(self.ctx)


class 단계2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[3000], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='main') == 5:
            return 단계시작2(self.ctx)


class 단계시작2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=103, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return 단계조건체크몬스터2(self.ctx)


class 단계조건체크몬스터2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[109])
        self.add_balloon_talk(spawn_id=107, msg='$02000543_BF__MAIN__8$', duration=3500, delay_tick=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[109]):
            return 단계시작전1_3(self.ctx)


class 단계시작전1_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 단계시작전2_3(self.ctx)


class 단계시작전2_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_ai_extra_data(key='phaseSecond', value=5)
            self.set_ai_extra_data(key='phase', value=5)
            return 단계3(self.ctx)


class 단계3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02000543_BF__MAIN__9$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 조건체크몬스터스폰(self.ctx)


class 조건체크몬스터스폰(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=21450036, illust='DesertDragonMagicGreen_normal', duration=4000, script='$02000543_BF__MAIN__10$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='main') == 8:
            return 응접실문열기전몬스터스폰(self.ctx)


class 응접실문열기전몬스터스폰(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101,102])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101,102]):
            return 응접실문대기(self.ctx)


class 응접실문대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ambient_light(primary=Vector3(201,38,70))
        self.set_onetime_effect(id=106, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_event_ui_script(type=BannerType.Text, script='$02000543_BF__MAIN__11$', duration=3000)
        self.destroy_monster(spawn_ids=[106,107])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 응접실문열기1(self.ctx)


class 응접실문열기1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[3003], visible=True)
        self.lock_my_pc(is_lock=True)
        self.side_npc_talk(npc_id=21450036, illust='DesertDragonMagicGreen_normal', duration=3000, script='$02000543_BF__MAIN__12$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 응접실문열기11(self.ctx)


class 응접실문열기11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[3000])
        self.set_effect(trigger_ids=[3002])
        self.set_effect(trigger_ids=[3004], visible=True)
        self.set_effect(trigger_ids=[3005], visible=True)
        self.side_npc_talk(npc_id=21450036, illust='DesertDragonMagicGreen_normal', duration=4000, script='$02000543_BF__MAIN__13$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 응접실문열기31(self.ctx)


class 응접실문열기31(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02000543_BF__MAIN__14$', duration=3000)
        self.destroy_monster(spawn_ids=[111,112])
        self.set_effect(trigger_ids=[3004])
        self.set_effect(trigger_ids=[3005])
        self.lock_my_pc()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 응접실문열기4(self.ctx)


class 응접실문열기4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=102, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_skill(trigger_ids=[4001], enable=True)
        self.set_effect(trigger_ids=[3003])
        self.add_balloon_talk(spawn_id=104, msg='$02000543_BF__MAIN__15$', duration=3500)
        self.add_balloon_talk(spawn_id=105, msg='$02000543_BF__MAIN__16$', duration=3500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 응접실문열고나서처리(self.ctx)


class 응접실문열고나서처리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11004644, illust='SlaveMan3_normal', duration=4000, script='$02000543_BF__MAIN__17$')
        self.destroy_monster(spawn_ids=[104,105])
        self.enable_spawn_point_pc(spawn_id=0)
        self.enable_spawn_point_pc(spawn_id=1, is_enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[702], job_code=0):
            return 보스스폰(self.ctx)


class 보스스폰(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=102, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=103, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 보스스폰2(self.ctx)


class 보스스폰2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=103, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.spawn_monster(spawn_ids=[103])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[103]):
            return 포탈열기(self.ctx)


class 포탈열기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)


initial_state = idle
