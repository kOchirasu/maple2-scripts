""" trigger/83000003_colosseum/main.xml """
import trigger_api
from System.Numerics import Vector3


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_user_value(trigger_id=900001, key='Reset', value=0)
        pass

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MainStart') == 1:
            self.set_user_value(trigger_id=900001, key='MainStart', value=0)
            self.destroy_monster(spawn_ids=[203])
            self.spawn_monster(spawn_ids=[202], auto_target=False)
            return WaitRound1(self.ctx)
        if self.user_value(key='MainStart') == 2:
            self.set_user_value(trigger_id=900001, key='MainStart', value=0)
            self.destroy_monster(spawn_ids=[203])
            self.spawn_monster(spawn_ids=[202], auto_target=False)
            return ContinuePlayDelay(self.ctx)


class WaitRound1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_user_value(trigger_id=910001, key='StartRound1', value=1)
            return ResultRound1(self.ctx)
        if self.user_detected(box_ids=[902]):
            self.move_user_to_pos(pos=Vector3(300,-225,1500), rot=Vector3(0,0,270))
            return WaitRound1(self.ctx)


class ContinuePlayDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.lock_my_pc(is_lock=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.move_user_to_pos(pos=Vector3(300,-225,1500), rot=Vector3(0,0,270))
            return ContinuePlayDelay2(self.ctx)


class ContinuePlayDelay2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.move_user_path(patrol_name='MS2PatrolData_01')
            return ContinuePlay(self.ctx)


class ContinuePlay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value_from_dungeon_reward_count(key='ClearRound', dungeon_reward_id=24096001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ClearRound') == 1:
            # self.debug_string(value='이어하기로 2스테이지 부터 시작합니다.')
            self.set_user_value(trigger_id=910002, key='StartRound2', value=1)
            return ResultRound2(self.ctx)
        if self.user_value(key='ClearRound') == 2:
            # self.debug_string(value='이어하기로 3스테이지 부터 시작합니다.')
            self.set_user_value(trigger_id=910003, key='StartRound3', value=1)
            return ResultRound3(self.ctx)
        if self.user_value(key='ClearRound') == 3:
            # self.debug_string(value='이어하기로 4스테이지 부터 시작합니다.')
            self.set_user_value(trigger_id=910004, key='StartRound4', value=1)
            return ResultRound4(self.ctx)
        if self.user_value(key='ClearRound') == 4:
            # self.debug_string(value='이어하기로 5스테이지 부터 시작합니다.')
            self.set_user_value(trigger_id=910005, key='StartRound5', value=1)
            return ResultRound5(self.ctx)
        if self.user_value(key='ClearRound') == 5:
            # self.debug_string(value='이어하기로 6스테이지 부터 시작합니다.')
            self.set_user_value(trigger_id=910006, key='StartRound6', value=1)
            return ResultRound6(self.ctx)
        if self.user_value(key='ClearRound') == 6:
            # self.debug_string(value='이어하기로 7스테이지 부터 시작합니다.')
            self.set_user_value(trigger_id=910007, key='StartRound7', value=1)
            return ResultRound7(self.ctx)
        if self.user_value(key='ClearRound') == 7:
            # self.debug_string(value='이어하기로 8스테이지 부터 시작합니다.')
            self.set_user_value(trigger_id=910008, key='StartRound8', value=1)
            return ResultRound8(self.ctx)
        if self.user_value(key='ClearRound') == 8:
            # self.debug_string(value='이어하기로 9스테이지 부터 시작합니다.')
            self.set_user_value(trigger_id=910009, key='StartRound9', value=1)
            return ResultRound9(self.ctx)
        if self.user_value(key='ClearRound') == 9:
            # self.debug_string(value='이어하기로 10스테이지 부터 시작합니다.')
            self.set_user_value(trigger_id=910010, key='StartRound10', value=1)
            return ResultRound10(self.ctx)
        if self.user_value(key='ClearRound') == 10:
            # self.debug_string(value='이어하기로 11스테이지 부터 시작합니다.')
            self.set_user_value(trigger_id=910011, key='StartRound11', value=1)
            return ResultRound11(self.ctx)
        if self.user_value(key='ClearRound') == 11:
            # self.debug_string(value='이어하기로 12스테이지 부터 시작합니다.')
            self.set_user_value(trigger_id=910012, key='StartRound12', value=1)
            return ResultRound12(self.ctx)
        if self.user_value(key='ClearRound') == 12:
            # self.debug_string(value='이어하기로 13스테이지 부터 시작합니다.')
            self.set_user_value(trigger_id=910013, key='StartRound13', value=1)
            return ResultRound13(self.ctx)
        if self.user_value(key='ClearRound') == 13:
            # self.debug_string(value='이미 13 스테이지까지 완료 했습니다. 처음부터 시작합니다. ')
            return WaitRound1(self.ctx)


class ResultRound1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartRound1') == 2:
            self.dungeon_clear_round(round=1)
            self.set_user_value(trigger_id=910001, key='StartRound1', value=0)
            self.set_user_value(trigger_id=900001, key='StartRound1', value=0)
            return WaitRound2(self.ctx)
        if self.user_value(key='StartRound1') == 3:
            self.dungeon_clear_round(round=0)
            self.set_user_value(trigger_id=910001, key='StartRound1', value=0)
            self.set_user_value(trigger_id=900001, key='StartRound1', value=0)
            return RoundFail(self.ctx)


class WaitRound2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_user_value(trigger_id=910002, key='StartRound2', value=1)
            return ResultRound2(self.ctx)


class ResultRound2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartRound2') == 2:
            self.dungeon_clear_round(round=2)
            self.set_user_value(trigger_id=910002, key='StartRound2', value=0)
            self.set_user_value(trigger_id=900001, key='StartRound2', value=0)
            return WaitRound3(self.ctx)
        if self.user_value(key='StartRound2') == 3:
            self.set_user_value(trigger_id=910002, key='StartRound2', value=0)
            self.set_user_value(trigger_id=900001, key='StartRound2', value=0)
            return RoundClear1(self.ctx)


class WaitRound3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_user_value(trigger_id=910003, key='StartRound3', value=1)
            return ResultRound3(self.ctx)


class ResultRound3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartRound3') == 2:
            self.dungeon_clear_round(round=3)
            self.set_user_value(trigger_id=910003, key='StartRound3', value=0)
            self.set_user_value(trigger_id=900001, key='StartRound3', value=0)
            return WaitRound4(self.ctx)
        if self.user_value(key='StartRound3') == 3:
            self.set_user_value(trigger_id=910003, key='StartRound3', value=0)
            self.set_user_value(trigger_id=900001, key='StartRound3', value=0)
            return RoundClear2(self.ctx)


class WaitRound4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_user_value(trigger_id=910004, key='StartRound4', value=1)
            return ResultRound4(self.ctx)


class ResultRound4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartRound4') == 2:
            self.dungeon_clear_round(round=4)
            self.set_user_value(trigger_id=910004, key='StartRound4', value=0)
            self.set_user_value(trigger_id=900001, key='StartRound4', value=0)
            return WaitRound5(self.ctx)
        if self.user_value(key='StartRound4') == 3:
            self.set_user_value(trigger_id=910004, key='StartRound4', value=0)
            self.set_user_value(trigger_id=900001, key='StartRound4', value=0)
            return RoundClear3(self.ctx)


class WaitRound5(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_user_value(trigger_id=910005, key='StartRound5', value=1)
            return ResultRound5(self.ctx)


class ResultRound5(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartRound5') == 2:
            self.dungeon_clear_round(round=5)
            self.set_user_value(trigger_id=910005, key='StartRound5', value=0)
            self.set_user_value(trigger_id=900001, key='StartRound5', value=0)
            return WaitRound6(self.ctx)
        if self.user_value(key='StartRound5') == 3:
            self.set_user_value(trigger_id=910005, key='StartRound5', value=0)
            self.set_user_value(trigger_id=900001, key='StartRound5', value=0)
            return RoundClear4(self.ctx)


class WaitRound6(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_user_value(trigger_id=910006, key='StartRound6', value=1)
            return ResultRound6(self.ctx)


class ResultRound6(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartRound6') == 2:
            self.dungeon_clear_round(round=6)
            self.set_user_value(trigger_id=910006, key='StartRound6', value=0)
            self.set_user_value(trigger_id=900001, key='StartRound6', value=0)
            return WaitRound7(self.ctx)
        if self.user_value(key='StartRound6') == 3:
            self.set_user_value(trigger_id=910006, key='StartRound6', value=0)
            self.set_user_value(trigger_id=900001, key='StartRound6', value=0)
            return RoundClear5(self.ctx)


class WaitRound7(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_user_value(trigger_id=910007, key='StartRound7', value=1)
            return ResultRound7(self.ctx)


class ResultRound7(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartRound7') == 2:
            self.dungeon_clear_round(round=7)
            self.set_user_value(trigger_id=910007, key='StartRound7', value=0)
            self.set_user_value(trigger_id=900001, key='StartRound7', value=0)
            return WaitRound8(self.ctx)
        if self.user_value(key='StartRound7') == 3:
            self.set_user_value(trigger_id=910007, key='StartRound7', value=0)
            self.set_user_value(trigger_id=900001, key='StartRound7', value=0)
            return RoundClear6(self.ctx)


class WaitRound8(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_user_value(trigger_id=910008, key='StartRound8', value=1)
            return ResultRound8(self.ctx)


class ResultRound8(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartRound8') == 2:
            self.dungeon_clear_round(round=8)
            self.set_user_value(trigger_id=910008, key='StartRound8', value=0)
            self.set_user_value(trigger_id=900001, key='StartRound8', value=0)
            return WaitRound9(self.ctx)
        if self.user_value(key='StartRound8') == 3:
            self.set_user_value(trigger_id=910008, key='StartRound8', value=0)
            self.set_user_value(trigger_id=900001, key='StartRound8', value=0)
            return RoundClear7(self.ctx)


class WaitRound9(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_user_value(trigger_id=910009, key='StartRound9', value=1)
            return ResultRound9(self.ctx)


class ResultRound9(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartRound9') == 2:
            self.dungeon_clear_round(round=9)
            self.set_user_value(trigger_id=910009, key='StartRound9', value=0)
            self.set_user_value(trigger_id=900001, key='StartRound9', value=0)
            return WaitRound10(self.ctx)
        if self.user_value(key='StartRound9') == 3:
            self.set_user_value(trigger_id=910009, key='StartRound9', value=0)
            self.set_user_value(trigger_id=900001, key='StartRound9', value=0)
            return RoundClear8(self.ctx)


class WaitRound10(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_user_value(trigger_id=910010, key='StartRound10', value=1)
            return ResultRound10(self.ctx)


class ResultRound10(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartRound10') == 2:
            self.dungeon_clear_round(round=10)
            self.set_user_value(trigger_id=910010, key='StartRound10', value=0)
            self.set_user_value(trigger_id=900001, key='StartRound10', value=0)
            return WaitRound11(self.ctx)
        if self.user_value(key='StartRound10') == 3:
            self.set_user_value(trigger_id=910010, key='StartRound10', value=0)
            self.set_user_value(trigger_id=900001, key='StartRound10', value=0)
            return RoundClear9(self.ctx)


class WaitRound11(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_user_value(trigger_id=910011, key='StartRound11', value=1)
            return ResultRound11(self.ctx)


class ResultRound11(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartRound11') == 2:
            self.dungeon_clear_round(round=11)
            self.set_user_value(trigger_id=910011, key='StartRound11', value=0)
            self.set_user_value(trigger_id=900001, key='StartRound11', value=0)
            return WaitRound12(self.ctx)
        if self.user_value(key='StartRound11') == 3:
            self.set_user_value(trigger_id=910011, key='StartRound11', value=0)
            self.set_user_value(trigger_id=900001, key='StartRound11', value=0)
            return RoundClear10(self.ctx)


class WaitRound12(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_user_value(trigger_id=910012, key='StartRound12', value=1)
            return ResultRound12(self.ctx)


class ResultRound12(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartRound12') == 2:
            self.dungeon_clear_round(round=12)
            self.set_user_value(trigger_id=910012, key='StartRound12', value=0)
            self.set_user_value(trigger_id=900001, key='StartRound12', value=0)
            return WaitRound13(self.ctx)
        if self.user_value(key='StartRound12') == 3:
            self.set_user_value(trigger_id=910012, key='StartRound12', value=0)
            self.set_user_value(trigger_id=900001, key='StartRound12', value=0)
            return RoundClear11(self.ctx)


class WaitRound13(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_user_value(trigger_id=910013, key='StartRound13', value=1)
            return ResultRound13(self.ctx)


class ResultRound13(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartRound13') == 2:
            self.dungeon_clear_round(round=13)
            self.set_user_value(trigger_id=910013, key='StartRound13', value=0)
            self.set_user_value(trigger_id=900001, key='StartRound13', value=0)
            return AllRoundClear(self.ctx)
        if self.user_value(key='StartRound13') == 3:
            self.set_user_value(trigger_id=910013, key='StartRound13', value=0)
            self.set_user_value(trigger_id=900001, key='StartRound13', value=0)
            return RoundClear12(self.ctx)


class RoundClear1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear(ui_type='None')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 대기(self.ctx)


class RoundClear2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear(ui_type='None')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 대기(self.ctx)


class RoundClear3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear(ui_type='None')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 대기(self.ctx)


class RoundClear4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear(ui_type='None')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 대기(self.ctx)


class RoundClear5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear(ui_type='None')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 대기(self.ctx)


class RoundClear6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear(ui_type='None')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 대기(self.ctx)


class RoundClear7(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear(ui_type='None')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 대기(self.ctx)


class RoundClear8(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear(ui_type='None')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 대기(self.ctx)


class RoundClear9(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear(ui_type='None')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 대기(self.ctx)


class RoundClear10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear(ui_type='None')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 대기(self.ctx)


class RoundClear11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear(ui_type='None')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 대기(self.ctx)


class RoundClear12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear(ui_type='None')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 대기(self.ctx)


class AllRoundClear(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 대기(self.ctx)


class RoundFail(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_fail()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 대기(self.ctx)


initial_state = 대기
