""" trigger/80000014_bonus/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001337], state=1)
        self.set_interact_object(trigger_ids=[10001338], state=2)
        self.set_portal(portal_id=2)
        self.set_mesh(trigger_ids=[3000,3001], visible=True)
        self.set_mesh(trigger_ids=[3002,3003,3004])
        self.set_mesh(trigger_ids=[3101,3102,3201,3202,3301,3302,3401,3402,3601,3602,3603,3604])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199]):
            # self.set_timer(timer_id='30', seconds=600, start_delay=1, interval=1, v_offset=80)
            return 랜덤A(self.ctx)


class 랜덤A(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=50.0):
            self.set_mesh(trigger_ids=[3101], visible=True)
            return 랜덤B(self.ctx)
        if self.random_condition(weight=50.0):
            self.set_mesh(trigger_ids=[3102], visible=True)
            return 랜덤B(self.ctx)


class 랜덤B(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=50.0):
            self.set_mesh(trigger_ids=[3201], visible=True)
            return 랜덤C(self.ctx)
        if self.random_condition(weight=50.0):
            self.set_mesh(trigger_ids=[3202], visible=True)
            return 랜덤C(self.ctx)


class 랜덤C(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=50.0):
            self.set_mesh(trigger_ids=[3301], visible=True)
            return 랜덤D(self.ctx)
        if self.random_condition(weight=50.0):
            self.set_mesh(trigger_ids=[3302], visible=True)
            return 랜덤D(self.ctx)


class 랜덤D(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=50.0):
            self.set_mesh(trigger_ids=[3401], visible=True)
            return 랜덤E(self.ctx)
        if self.random_condition(weight=50.0):
            self.set_mesh(trigger_ids=[3402], visible=True)
            return 랜덤E(self.ctx)


class 랜덤E(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=50.0):
            self.set_mesh(trigger_ids=[3601,3602], visible=True)
            return 시작(self.ctx)
        if self.random_condition(weight=50.0):
            self.set_mesh(trigger_ids=[3603,3604], visible=True)
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$80000014_bonus__main__0$', arg3='5000')
        self.score_board_create(type='ScoreBoardTopCenter')
        self.score_board_set_score(score=0)
        self.spawn_item_range(range_ids=[9001,9002,9003,9004,9005,9006,9007,9008,9009,9010,9011,9012,9013,9014,9015,9016,9017,9018,9019], random_pick_count=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[102]):
            return 보스등장(self.ctx)


class 보스등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_npc_range(range_ids=[2001], score=1500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 딜레이(self.ctx)


class 딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[0])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            self.set_mesh(trigger_ids=[3000,3001])
            self.set_mesh(trigger_ids=[3002,3003,3004], visible=True)
            return 정산(self.ctx)


class 정산(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.score_board_score() >= 18000:
            self.debug_string(value='18000 이상')
            self.set_achievement(trigger_id=199, type='trigger', achieve='HighScoreTreasureMap01')
            self.set_achievement(trigger_id=199, type='trigger', achieve='TimerunTreasureMap01')
            # self.set_event_ui(type=7, arg2='미션 성공! 참 잘했어요!', arg3='2500')
            return 반응대기(self.ctx)
        if self.score_board_score() < 18000:
            self.debug_string(value='18000 미만')
            self.set_achievement(trigger_id=199, type='trigger', achieve='TimerunTreasureMap01')
            # self.set_event_ui(type=7, arg2='미션 성공!', arg3='2500')
            return 반응대기(self.ctx)
        if self.wait_tick(wait_tick=500):
            return 반응대기(self.ctx)


class 반응대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001338], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001338], state=0):
            self.set_achievement(trigger_id=199, type='trigger', achieve='TreasureMap01')
            self.dungeon_clear()
            self.score_board_remove()
            self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
