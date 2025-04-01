""" trigger/99999841/team2_battle.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dungeon_variable(var_id=3, value=0)
        self.set_dungeon_variable(var_id=200, value=0)
        self.set_interact_object(trigger_ids=[10002182], state=1)
        self.start_combine_spawn(group_id=[513])
        self.start_combine_spawn(group_id=[514])
        self.start_combine_spawn(group_id=[515])
        self.set_user_value(trigger_id=99990001, key='Team2Win', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Team2Battle') == 1:
            return 지역선택1(self.ctx)


class 지역선택1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.score_board_create(max_score=240)
        # self.set_timer(timer_id='1', seconds=60, auto_remove=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=2) == 1:
            return 종료(self.ctx)
        if self.random_condition(weight=33.0):
            return A지역1(self.ctx)
        if self.random_condition(weight=34.0):
            return B지역1(self.ctx)
        if self.random_condition(weight=33.0):
            return C지역1(self.ctx)


class A지역1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[513], is_start=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=2) == 1:
            return 종료(self.ctx)
        if self.object_interacted(interact_ids=[10002182], state=0):
            return 시작_보스전(self.ctx)
        """
        if self.time_expired(timer_id='1'):
            self.reset_timer(timer_id='1')
            return 지역선택2_1(self.ctx)
        """
        if self.score_board_score() >= 100:
            return 지역선택2_1(self.ctx)


class B지역1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[514], is_start=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=2) == 1:
            return 종료(self.ctx)
        if self.object_interacted(interact_ids=[10002182], state=0):
            return 시작_보스전(self.ctx)
        """
        if self.time_expired(timer_id='1'):
            self.reset_timer(timer_id='1')
            return 지역선택2_2(self.ctx)
        """
        if self.score_board_score() >= 100:
            return 지역선택2_2(self.ctx)


class C지역1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[515], is_start=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=2) == 1:
            return 종료(self.ctx)
        if self.object_interacted(interact_ids=[10002182], state=0):
            return 시작_보스전(self.ctx)
        """
        if self.time_expired(timer_id='1'):
            self.reset_timer(timer_id='1')
            return 지역선택2_3(self.ctx)
        """
        if self.score_board_score() >= 100:
            return 지역선택2_3(self.ctx)


class 지역선택2_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='추가 병력 등장', duration=4000, box_ids=['9201'])
        # self.set_timer(timer_id='2', seconds=60, auto_remove=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=2) == 1:
            return 종료(self.ctx)
        if self.object_interacted(interact_ids=[10002182], state=0):
            return 시작_보스전(self.ctx)
        if self.random_condition(weight=50.0):
            return B지역2(self.ctx)
        if self.random_condition(weight=50.0):
            return C지역2(self.ctx)


class 지역선택2_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='추가 병력 등장', duration=4000, box_ids=['9201'])
        # self.set_timer(timer_id='2', seconds=60, auto_remove=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=2) == 1:
            return 종료(self.ctx)
        if self.object_interacted(interact_ids=[10002182], state=0):
            return 시작_보스전(self.ctx)
        if self.random_condition(weight=50.0):
            return A지역2(self.ctx)
        if self.random_condition(weight=50.0):
            return C지역2(self.ctx)


class 지역선택2_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='추가 병력 등장', duration=4000, box_ids=['9201'])
        # self.set_timer(timer_id='2', seconds=60, auto_remove=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=2) == 1:
            return 종료(self.ctx)
        if self.object_interacted(interact_ids=[10002182], state=0):
            return 시작_보스전(self.ctx)
        if self.random_condition(weight=50.0):
            return A지역2(self.ctx)
        if self.random_condition(weight=50.0):
            return B지역2(self.ctx)


class A지역2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[513], is_start=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=2) == 1:
            return 종료(self.ctx)
        if self.object_interacted(interact_ids=[10002182], state=0):
            return 시작_보스전(self.ctx)
        """
        if self.time_expired(timer_id='2'):
            self.reset_timer(timer_id='2')
            return 지역선택3_1(self.ctx)
        """
        if self.score_board_score() >= 240:
            self.score_board_remove()
            return 지역선택3_1(self.ctx)


class B지역2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[514], is_start=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=2) == 1:
            return 종료(self.ctx)
        if self.object_interacted(interact_ids=[10002182], state=0):
            return 시작_보스전(self.ctx)
        """
        if self.time_expired(timer_id='2'):
            self.reset_timer(timer_id='2')
            return 지역선택3_2(self.ctx)
        """
        if self.score_board_score() >= 240:
            self.score_board_remove()
            return 지역선택3_2(self.ctx)


class C지역2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[515], is_start=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=2) == 1:
            return 종료(self.ctx)
        if self.object_interacted(interact_ids=[10002182], state=0):
            return 시작_보스전(self.ctx)
        """
        if self.time_expired(timer_id='2'):
            self.reset_timer(timer_id='2')
            return 지역선택3_3(self.ctx)
        """
        if self.score_board_score() >= 240:
            self.score_board_remove()
            return 지역선택3_3(self.ctx)


class 지역선택3_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dungeon_variable(var_id=2000, value=1)
        # self.set_event_ui_script(type=BannerType.Text, script='상대편 지역으로 침투할 수 있는 포탈이 생성되었습니다.\\n한 명만 갈 수 있습니다.', duration=4000, box_ids=['9201'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=2) == 1:
            return 종료(self.ctx)
        if self.object_interacted(interact_ids=[10002182], state=0):
            return 시작_보스전(self.ctx)
        if self.random_condition(weight=50.0):
            return B지역3(self.ctx)
        if self.random_condition(weight=50.0):
            return C지역3(self.ctx)


class 지역선택3_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dungeon_variable(var_id=2000, value=1)
        # self.set_event_ui_script(type=BannerType.Text, script='상대편 지역으로 침투할 수 있는 포탈이 생성되었습니다.\\n한 명만 갈 수 있습니다.', duration=4000, box_ids=['9201'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=2) == 1:
            return 종료(self.ctx)
        if self.object_interacted(interact_ids=[10002182], state=0):
            return 시작_보스전(self.ctx)
        if self.random_condition(weight=50.0):
            return A지역3(self.ctx)
        if self.random_condition(weight=50.0):
            return C지역3(self.ctx)


class 지역선택3_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dungeon_variable(var_id=2000, value=1)
        # self.set_event_ui_script(type=BannerType.Text, script='상대편 지역으로 침투할 수 있는 포탈이 생성되었습니다.\\n한 명만 갈 수 있습니다.', duration=4000, box_ids=['9201'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=2) == 1:
            return 종료(self.ctx)
        if self.object_interacted(interact_ids=[10002182], state=0):
            return 시작_보스전(self.ctx)
        if self.random_condition(weight=50.0):
            return A지역3(self.ctx)
        if self.random_condition(weight=50.0):
            return B지역3(self.ctx)


class A지역3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[513], is_start=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=2) == 1:
            return 종료(self.ctx)
        if self.object_interacted(interact_ids=[10002182], state=0):
            return 시작_보스전(self.ctx)


class B지역3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[514], is_start=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=2) == 1:
            return 종료(self.ctx)
        if self.object_interacted(interact_ids=[10002182], state=0):
            return 시작_보스전(self.ctx)


class C지역3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[515], is_start=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=2) == 1:
            return 종료(self.ctx)
        if self.object_interacted(interact_ids=[10002182], state=0):
            return 시작_보스전(self.ctx)


class 시작_보스전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10002179], state=0)
        self.set_interact_object(trigger_ids=[10002180], state=0)
        self.set_interact_object(trigger_ids=[10002181], state=0)
        self.set_interact_object(trigger_ids=[10002182], state=0)
        self.start_combine_spawn(group_id=[513])
        self.start_combine_spawn(group_id=[514])
        self.start_combine_spawn(group_id=[515])
        self.spawn_monster(spawn_ids=[911], auto_target=False)
        self.set_dungeon_variable(var_id=200, value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=2) == 1:
            return 종료(self.ctx)
        if self.monster_dead(spawn_ids=[911]):
            return 성공(self.ctx)


class 성공(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dungeon_variable(var_id=3, value=1)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10002179], state=0)
        self.set_interact_object(trigger_ids=[10002180], state=0)
        self.set_interact_object(trigger_ids=[10002181], state=0)
        self.set_interact_object(trigger_ids=[10002182], state=0)
        self.start_combine_spawn(group_id=[513])
        self.start_combine_spawn(group_id=[514])
        self.start_combine_spawn(group_id=[515])
        self.destroy_monster(spawn_ids=[911])


initial_state = 대기
