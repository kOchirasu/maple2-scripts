""" trigger/02000537_bf/main.xml """
import trigger_api


"""
심연의 성채
플레이어 감지
"""
class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[5000], visible=True)
        self.set_mesh(trigger_ids=[8900], visible=True)
        self.set_mesh(trigger_ids=[8901], visible=True)
        self.set_mesh(trigger_ids=[8902], visible=True)
        self.set_mesh(trigger_ids=[8903], visible=True)
        self.set_mesh(trigger_ids=[8904], visible=True)
        self.set_mesh(trigger_ids=[8905], visible=True)
        self.set_effect(trigger_ids=[8000])
        self.set_effect(trigger_ids=[8001])
        self.set_skill(trigger_ids=[9000])
        self.enable_spawn_point_pc(spawn_id=0, is_enable=True)
        self.enable_spawn_point_pc(spawn_id=1)
        self.enable_spawn_point_pc(spawn_id=2)
        self.enable_spawn_point_pc(spawn_id=3)
        self.enable_spawn_point_pc(spawn_id=4)
        self.enable_spawn_point_pc(spawn_id=5)
        self.enable_spawn_point_pc(spawn_id=6)
        self.set_portal(portal_id=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[701], job_code=0):
            return ready(self.ctx)


# 첫번째 발판
class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000537_BF__MAIN__0$', arg3='3000')
        self.spawn_monster(spawn_ids=[101,1011,1012,1013,1014,1017,1018,1019], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101,1011,1012,1013,1014,1017,1018,1019]):
            return 도마뱀스폰1(self.ctx)


class 도마뱀스폰1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8900])
        self.spawn_monster(spawn_ids=[1015,1016])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[702], job_code=0):
            return 시작702(self.ctx)


class 시작702(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.enable_spawn_point_pc(spawn_id=0)
        self.enable_spawn_point_pc(spawn_id=1, is_enable=True)
        self.spawn_monster(spawn_ids=[102,1022,1023,1024,1025])
        self.side_npc_talk(npc_id=22600006, illust='DesertDragonBigBlue_normal', duration=4000, script='$02000537_BF__MAIN__1$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[102,1022,1023,1024,1025]):
            return 마무리1_702(self.ctx)


class 마무리1_702(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8901])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 마무리2_702(self.ctx)


class 마무리2_702(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11004643, illust='SlaveWoman3_normal', duration=4000, script='$02000537_BF__MAIN__2$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[703], job_code=0):
            return 시작703(self.ctx)


class 시작703(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1026])
        self.enable_spawn_point_pc(spawn_id=1)
        self.enable_spawn_point_pc(spawn_id=2, is_enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 진행703(self.ctx)


class 진행703(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000537_BF__MAIN__3$', arg3='3000')
        self.spawn_monster(spawn_ids=[109])
        self.spawn_monster(spawn_ids=[103,1031,1032,1033,1034])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[103,1031,1032,1033,1034]):
            return 마무리1_703(self.ctx)


class 마무리1_703(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8902])
        self.spawn_monster(spawn_ids=[1035])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 마무리2_703(self.ctx)


class 마무리2_703(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11004644, illust='SlaveMan3_normal', duration=4000, script='$02000537_BF__MAIN__4$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[704], job_code=0):
            return 시작704(self.ctx)


class 시작704(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.enable_spawn_point_pc(spawn_id=2)
        self.enable_spawn_point_pc(spawn_id=3, is_enable=True)
        self.spawn_monster(spawn_ids=[104,1041,1042,1043,1044], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 진행704(self.ctx)


class 진행704(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11004643, illust='SlaveWoman3_normal', duration=4000, script='$02000537_BF__MAIN__5$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[104,1041,1042,1043,1044]):
            return 마무리704(self.ctx)


class 마무리704(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8903])
        self.side_npc_talk(npc_id=11004643, illust='SlaveWoman3_normal', duration=4000, script='$02000537_BF__MAIN__6$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[705], job_code=0):
            return 시작705(self.ctx)


class 시작705(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.enable_spawn_point_pc(spawn_id=3)
        self.enable_spawn_point_pc(spawn_id=4, is_enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 진행705(self.ctx)


class 진행705(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[105,1051,1052,1053,1054])
        self.side_npc_talk(npc_id=22600006, illust='DesertDragonBigBlue_normal', duration=4000, script='$02000537_BF__MAIN__7$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[105,1051,1052,1053,1054]):
            return 마무리705(self.ctx)


class 마무리705(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8904])
        self.spawn_monster(spawn_ids=[1036])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[708], job_code=0):
            return 버프걸어주기(self.ctx)


class 버프걸어주기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11004644, illust='SlaveMan3_normal', duration=4000, script='$02000537_BF__MAIN__8$')
        self.set_skill(trigger_ids=[9000], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[706], job_code=0):
            return 시작706(self.ctx)


class 시작706(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11004643, illust='SlaveWoman3_normal', duration=4000, script='$02000537_BF__MAIN__9$')
        self.enable_spawn_point_pc(spawn_id=4)
        self.enable_spawn_point_pc(spawn_id=5, is_enable=True)
        self.spawn_monster(spawn_ids=[106,1061,1063,1064,1065])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[106,1061,1063,1064,1065]):
            return 마무리706(self.ctx)


class 마무리706(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8905])
        self.side_npc_talk(npc_id=11004644, illust='SlaveMan3_normal', duration=4000, script='$02000537_BF__MAIN__10$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[707], job_code=0):
            return 시작707(self.ctx)


class 시작707(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.enable_spawn_point_pc(spawn_id=5)
        self.enable_spawn_point_pc(spawn_id=6, is_enable=True)
        self.spawn_monster(spawn_ids=[108])
        self.side_npc_talk(npc_id=22600006, illust='DesertDragonBigBlue_normal', duration=4000, script='$02000537_BF__MAIN__11$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[108]):
            return 포털생성전(self.ctx)


class 포털생성전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[109])
        self.spawn_monster(spawn_ids=[1091])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 포털생성전2(self.ctx)


class 포털생성전2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[109])
        self.spawn_monster(spawn_ids=[1091])
        self.side_npc_talk(npc_id=11004643, illust='SlaveWoman3_normal', duration=4000, script='$02000537_BF__MAIN__12$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 포털생성(self.ctx)


class 포털생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)


initial_state = idle
