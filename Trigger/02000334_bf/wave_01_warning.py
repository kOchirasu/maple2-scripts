""" trigger/02000334_bf/wave_01_warning.xml """
import trigger_api


# 플레이어 감지
class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=90099, spawn_ids=[150]):
            return 차타이머1(self.ctx)
        if self.monster_dead(spawn_ids=[999]):
            return 게임오버(self.ctx)


class 차타이머1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='30', seconds=30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='30'):
            return 돌격(self.ctx)


# 몬스터 돌격 생성
class 돌격(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[98001], visible=True)
        self.move_npc(spawn_id=190, patrol_name='MS2PatrolData_3501') # 바라하 빡침 모션
        self.set_dialogue(type=1, spawn_id=190, script='$02000334_BF__WAVE__0$', time=3) # 보스 대사
        self.spawn_monster(spawn_ids=[991,992,993])
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 카메라_복구(self.ctx)


class 카메라_복구(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[98006], visible=True)
        self.move_npc(spawn_id=199, patrol_name='MS2PatrolData_3502') # 오스칼 대응 모션
        self.add_buff(box_ids=[90001], skill_id=70000068, level=1) # 이속 버프를 걸어준다
        self.set_dialogue(type=1, spawn_id=199, script='$02000334_BF__WAVE__1$', time=3) # 오스칼 대사
        self.select_camera_path(path_ids=[8017], return_view=False) # 사이드뷰 카메라


class 게임오버(trigger_api.Trigger):
    pass


initial_state = 시작
