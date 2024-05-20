""" trigger/99999999_bf/main.xml """
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
        if self.wait_tick(wait_tick=100):
            return 카메라경로(self.ctx)


class 카메라경로(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(is_visible=False)
        self.select_camera_path(path_ids=[7000,7001])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 카메라리셋(self.ctx)


class 카메라리셋(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=1.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[701], job_code=0):
            return ready(self.ctx)


# 첫번째 발판
class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(is_visible=True)
        self.set_event_ui(type=1, arg2='까마득한 성채를 따라 내려가야 합니다.\\n몰려오는 어둠을 조심하세요.', arg3='3000')
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
        self.side_npc_talk(npc_id=22600006, illust='DesertDragonBigBlue_normal', duration=4000, script='인간? 이게 얼마 만에 맡아보는 인간 냄새인지... 아주 향긋하군. 천천히 어둠 속으로 내려오라고.')

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
        self.side_npc_talk(npc_id=11004643, illust='SlaveWoman3_normal', duration=4000, script='불쌍한 인간... 샘은 이미 너를 주시하고 있어. 어둠이 너를 쫓을거야.')

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
        self.set_event_ui(type=1, arg2='어둠의 샘이 당신의 존재를 눈치챘습니다.\\n생명을 탐하는 검은 화살이 당신을 뒤쫓습니다.', arg3='3000')
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
        self.side_npc_talk(npc_id=11004644, illust='SlaveMan3_normal', duration=4000, script='수백년간 잠들어 있던 샘이 깨어났어. 샘은 영혼을 원해. 가까이 다가가지 않는게 좋아.')

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
        self.side_npc_talk(npc_id=11004643, illust='SlaveWoman3_normal', duration=4000, script='거미... 난 거미가 싫어... 거미는 영혼을 옭아매는 자...')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[104,1041,1042,1043,1044]):
            return 마무리704(self.ctx)


class 마무리704(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8903])
        self.side_npc_talk(npc_id=11004643, illust='SlaveWoman3_normal', duration=4000, script='샘은 거미의 눈을 빌려 모든걸 감시하고 있어. 조심하는게 좋아.')

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
        self.side_npc_talk(npc_id=22600006, illust='DesertDragonBigBlue_normal', duration=4000, script='얼마 안남았어. 조금 더... 조금 더 내려와봐.')

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
        self.side_npc_talk(npc_id=11004644, illust='SlaveMan3_normal', duration=4000, script='여기 들어온 순간...')
        self.set_skill(trigger_ids=[9000], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[706], job_code=0):
            return 시작706(self.ctx)


class 시작706(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11004643, illust='SlaveWoman3_normal', duration=4000, script='어둠을 만나게 되면... 다신 올라올 수 없어.')
        self.enable_spawn_point_pc(spawn_id=4)
        self.enable_spawn_point_pc(spawn_id=5, is_enable=True)
        self.spawn_monster(spawn_ids=[106,1061,1063,1064,1065])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[106,1061,1063,1064,1065]):
            return 마무리706(self.ctx)


class 마무리706(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8905])
        self.side_npc_talk(npc_id=11004644, illust='SlaveMan3_normal', duration=4000, script='그래 마치 우리처럼...')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[707], job_code=0):
            return 시작707(self.ctx)


class 시작707(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.enable_spawn_point_pc(spawn_id=5)
        self.enable_spawn_point_pc(spawn_id=6, is_enable=True)
        self.spawn_monster(spawn_ids=[108])
        self.side_npc_talk(npc_id=22600006, illust='DesertDragonBigBlue_normal', duration=4000, script='캬하하! 여기까지 오다니, 재미있겠는걸. 네 영혼도 여기에 묶어주마.')

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
        self.side_npc_talk(npc_id=11004643, illust='SlaveWoman3_normal', duration=4000, script='잠깐, 더 내려 갈거야? 여기서 어디로 갈지 우린 알 수 없어. 여긴 뒤틀린 미지의 공간. 모든 것은 샘의 뜻대로...')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 포털생성(self.ctx)


class 포털생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)


initial_state = idle
