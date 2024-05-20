""" trigger/02000542_bf/main.xml """
import trigger_api


# 플레이어 감지
class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2)
        self.enable_spawn_point_pc(spawn_id=0, is_enable=True)
        self.enable_spawn_point_pc(spawn_id=1)
        self.set_interact_object(trigger_ids=[10003142], state=1)
        self.set_interact_object(trigger_ids=[10003143], state=0)
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618], visible=True)
        self.set_mesh(trigger_ids=[619,620,621,622,623,624,625,626,627], visible=True)
        self.set_mesh(trigger_ids=[628,629,630,631,632,633,634,635,636], visible=True)
        self.set_onetime_effect(id=101, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=102, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=103, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[707], job_code=0):
            return 문열기오브젝트설정1(self.ctx)


class 문열기오브젝트설정1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000542_BF__MAIN__0$', arg3='5000')
        self.set_interact_object(trigger_ids=[10003142], state=1)
        self.spawn_monster(spawn_ids=[112], auto_target=False)
        self.add_balloon_talk(spawn_id=112, msg='$02000542_BF__MAIN__1$', duration=3500, delay_tick=1500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10003142], state=0):
            return 감옥문부시기1(self.ctx)


class 감옥문부시기1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11004643, illust='SlaveWoman3_normal', duration=4000, script='$02000542_BF__MAIN__2$')
        self.destroy_monster(spawn_ids=[112])
        self.set_onetime_effect(id=101, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_mesh(trigger_ids=[609])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[701], job_code=0):
            return 몬스터생성하기1(self.ctx)


class 몬스터생성하기1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=101, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.spawn_monster(spawn_ids=[101], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 문을열자1(self.ctx)


class 문을열자1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101]):
            return 감옥문부시기2(self.ctx)


class 감옥문부시기2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[605])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[702], job_code=0):
            return 몬스터생성하기2(self.ctx)


class 몬스터생성하기2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11004643, illust='SlaveWoman3_normal', duration=4000, script='$02000542_BF__MAIN__3$')
        self.spawn_monster(spawn_ids=[102])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[703], job_code=0):
            return 몬스터생성하기3(self.ctx)


class 몬스터생성하기3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11004643, illust='SlaveWoman3_normal', duration=4000, script='$02000542_BF__MAIN__4$')
        self.spawn_monster(spawn_ids=[103])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[704], job_code=0):
            return 몬스터생성하기4(self.ctx)


class 몬스터생성하기4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[104])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[102,103,104]):
            return 문열기오브젝트설정2(self.ctx)


class 문열기오브젝트설정2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000542_BF__MAIN__5$', arg3='5000')
        self.set_interact_object(trigger_ids=[10003143], state=1)
        self.spawn_monster(spawn_ids=[113], auto_target=False)
        self.add_balloon_talk(spawn_id=113, msg='$02000542_BF__MAIN__6$', duration=3500)
        self.add_balloon_talk(spawn_id=113, msg='$02000542_BF__MAIN__7$', duration=3500, delay_tick=3500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10003143], state=0):
            return 감옥문부시기3(self.ctx)


class 감옥문부시기3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=102, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_mesh(trigger_ids=[604])
        self.destroy_monster(spawn_ids=[113])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[708], job_code=0):
            return 감옥문부시기4(self.ctx)


class 감옥문부시기4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[116], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[116]):
            return 감옥문부시기5(self.ctx)


class 감옥문부시기5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[607])
        self.spawn_monster(spawn_ids=[121], auto_target=False)
        self.add_balloon_talk(spawn_id=121, msg='$02000542_BF__MAIN__8$', duration=8500, delay_tick=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[709], job_code=0):
            return 감옥문부시기6(self.ctx)


class 감옥문부시기6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[121])
        self.set_mesh(trigger_ids=[612])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[705], job_code=0):
            return 연출NPC스폰(self.ctx)


class 연출NPC스폰(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=102, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.spawn_monster(spawn_ids=[105,111], auto_target=False)
        self.add_balloon_talk(spawn_id=105, msg='$02000542_BF__MAIN__9$', duration=3500)
        self.add_balloon_talk(spawn_id=105, msg='$02000542_BF__MAIN__10$', duration=4500, delay_tick=3500)
        self.add_balloon_talk(spawn_id=111, msg='$02000542_BF__MAIN__11$', duration=3500, delay_tick=300)
        self.add_balloon_talk(spawn_id=111, msg='$02000542_BF__MAIN__12$', duration=4500, delay_tick=3800)
        self.spawn_monster(spawn_ids=[114], auto_target=False)
        self.side_npc_talk(npc_id=11004644, illust='SlaveMan3_normal', duration=4000, script='$02000542_BF__MAIN__13$')
        self.add_balloon_talk(spawn_id=114, msg='$02000542_BF__MAIN__14$', duration=4500, delay_tick=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[706], job_code=0):
            return 몬스터다수생성하기(self.ctx)


class 몬스터다수생성하기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[114])
        self.enable_spawn_point_pc(spawn_id=0)
        self.enable_spawn_point_pc(spawn_id=1, is_enable=True)
        self.spawn_monster(spawn_ids=[106,107,108,109], auto_target=False)
        self.spawn_monster(spawn_ids=[117,118,119,120], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[106,107,108,109]):
            return 보스스폰(self.ctx)


class 보스스폰(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=103, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.add_balloon_talk(spawn_id=117, msg='$02000542_BF__MAIN__15$', duration=8500, delay_tick=500)
        self.add_balloon_talk(spawn_id=118, msg='$02000542_BF__MAIN__16$', duration=8500, delay_tick=1000)
        self.add_balloon_talk(spawn_id=119, msg='$02000542_BF__MAIN__17$', duration=8500, delay_tick=1000)
        self.add_balloon_talk(spawn_id=120, msg='$02000542_BF__MAIN__18$', duration=8500, delay_tick=800)
        self.side_npc_talk(npc_id=11004644, illust='SlaveMan3_normal', duration=4000, script='$02000542_BF__MAIN__19$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 보스스폰2(self.ctx)


class 보스스폰2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=103, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.spawn_monster(spawn_ids=[110], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[110]):
            return 포탈열기(self.ctx)


class 포탈열기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 포탈열기2(self.ctx)


class 포탈열기2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[115], auto_target=False)
        self.destroy_monster(spawn_ids=[117,118,119,120])
        self.side_npc_talk(npc_id=11004643, illust='SlaveWoman3_normal', duration=4000, script='$02000542_BF__MAIN__20$')
        self.add_balloon_talk(spawn_id=115, msg='$02000542_BF__MAIN__21$', duration=3500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 포탈열기3(self.ctx)


class 포탈열기3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=103, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_mesh(trigger_ids=[601,602])
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
        self.destroy_monster(spawn_ids=[115])


initial_state = idle
