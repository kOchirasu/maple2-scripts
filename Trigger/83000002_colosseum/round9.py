""" trigger/83000002_colosseum/round9.xml """
import trigger_api
from System.Numerics import Vector3
from Maple2.Server.Game.Scripting.Trigger import BannerType


# 9라운드 바사라 첸
class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=11000)
        self.set_sound(trigger_id=11001)
        self.set_sound(trigger_id=12000)
        self.set_sound(trigger_id=12001)
        self.set_sound(trigger_id=13000)
        self.set_sound(trigger_id=13001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartRound9') == 1:
            return 시작딜레이(self.ctx)


class 시작딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 라운드조건체크(self.ctx)


class 라운드조건체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_round() == 9:
            self.side_npc_talk(npc_id=11004288, illust='nagi_normal', script='$83000002_COLOSSEUM__ROUND9__0$', duration=5000)
            # self.set_event_ui_script(type=BannerType.Text, script='전투에서 승리하셨습니다. 이제 부터는 벅찬 상대가 나올 수 있습니다. 마음 단단히 먹으십시오.', duration=3000)
            return 라운드대기(self.ctx)
        self.side_npc_talk(npc_id=11004288, illust='nagi_switchon', script='$83000002_COLOSSEUM__ROUND9__1$', duration=3000)
        self.debug_string(value='던전 요구 아이템 점수를 달성 못해 실패 처리 됩니다.')
        return FailRound(self.ctx)


class 라운드대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=11000, enable=True)
        self.set_sound(trigger_id=11001, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            self.side_npc_cutin(illust='VasaraChen_normal', duration=3000)
            self.show_round_ui(round=9, duration=3000)
            return 몬스터스폰대기(self.ctx)


class 몬스터스폰대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터스폰(self.ctx)


class 몬스터스폰(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[109], auto_target=False)
        self.add_buff(box_ids=[109], skill_id=69000501, level=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 카운트(self.ctx)


class 카운트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_count_ui(text='$83000002_COLOSSEUM__ROUND9__2$', count=3, sound_type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 전투시작(self.ctx)


"""
class 카운트2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='2', duration=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 카운트3(self.ctx)
"""

"""
class 카운트3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='1', duration=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 전투시작(self.ctx)
"""

class 전투시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.lock_my_pc()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 기믹더미소환(self.ctx)


class 기믹더미소환(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=50.0):
            self.spawn_monster(spawn_ids=[10000], auto_target=False)
            return 스폰대사(self.ctx)
        if self.random_condition(weight=50.0):
            self.spawn_monster(spawn_ids=[10001], auto_target=False)
            return 스폰대사(self.ctx)


class 스폰대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=109, msg='$83000002_COLOSSEUM__ROUND9__3$', duration=3000)
        self.set_timer(timer_id='LimitTimer', seconds=180, auto_remove=True)
        self.set_npc_duel_hp_bar(is_open=True, spawn_id=109, duration_tick=180000, npc_hp_step=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[109]):
            self.add_balloon_talk(spawn_id=109, msg='$83000002_COLOSSEUM__ROUND9__4$', duration=3000)
            self.set_npc_duel_hp_bar(spawn_id=109)
            self.destroy_monster(spawn_ids=[10000])
            self.destroy_monster(spawn_ids=[10001])
            return ClearRoundDelay(self.ctx)
        if self.time_expired(timer_id='LimitTimer'):
            # self.set_event_ui_script(type=BannerType.Text, script='경기시간이 경과했습니다. 도전에 실패 하였습니다. 전투를 종료합니다.', duration=3000)
            self.side_npc_talk(npc_id=11004288, illust='nagi_switchon', script='$83000002_COLOSSEUM__ROUND9__5$', duration=3000)
            self.destroy_monster(spawn_ids=[109])
            self.set_npc_duel_hp_bar(spawn_id=109)
            self.destroy_monster(spawn_ids=[10000])
            self.destroy_monster(spawn_ids=[10001])
            return FailRoundDelay(self.ctx)
        if self.user_detected(box_ids=[902]):
            # self.set_event_ui_script(type=BannerType.Text, script='경기장을 이탈했습니다. 전투가 종료됩니다. 다시 도전해 주세요.', duration=3000)
            self.side_npc_talk(npc_id=11004288, illust='nagi_switchon', script='$83000002_COLOSSEUM__ROUND9__6$', duration=3000)
            self.destroy_monster(spawn_ids=[109])
            self.set_npc_duel_hp_bar(spawn_id=109)
            self.destroy_monster(spawn_ids=[10000])
            self.destroy_monster(spawn_ids=[10001])
            return FailRoundDelay(self.ctx)
        if not self.user_detected(box_ids=[904]):
            self.set_event_ui_script(type=BannerType.Text, script='$83000002_COLOSSEUM__ROUND9__7$', duration=3000)
            self.side_npc_talk(npc_id=11004288, illust='nagi_switchon', script='$83000002_COLOSSEUM__ROUND9__8$', duration=3000)
            self.destroy_monster(spawn_ids=[109])
            self.set_npc_duel_hp_bar(spawn_id=109)
            self.destroy_monster(spawn_ids=[10000])
            self.destroy_monster(spawn_ids=[10001])
            return FailRoundDelay(self.ctx)


class ClearRoundDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.lock_my_pc(is_lock=True)
        self.set_sound(trigger_id=12000, enable=True)
        self.set_sound(trigger_id=12001, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.add_buff(box_ids=[904], skill_id=69000503, level=1, ignore_player=False, is_skill_set=False)
            self.set_event_ui_script(type=BannerType.Winner, script='$83000002_COLOSSEUM__ROUND9__9$', duration=3000)
            return ClearRound(self.ctx)


class FailRoundDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=13000, enable=True)
        self.set_sound(trigger_id=13001, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_event_ui_script(type=BannerType.GameOver, script='$83000002_COLOSSEUM__ROUND9__10$', duration=3000)
            return FailRound(self.ctx)


class ClearRound(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_event_ui_script(type=BannerType.Success, script='SUCCESS', duration=3000)
        pass

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.move_user_to_pos(pos=Vector3(300,-225,1500), rot=Vector3(0,0,270))
            # self.add_buff(box_ids=[904], skill_id=69000505, level=1, ignore_player=False, is_skill_set=False)
            self.side_npc_talk(npc_id=11004285, illust='Queencbean_Smile', script='$83000002_COLOSSEUM__ROUND9__11$', duration=3000)
            self.set_user_value(trigger_id=900001, key='StartRound9', value=2)
            return 이동대기(self.ctx)


class 이동대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.move_user_path(patrol_name='MS2PatrolData_01')
            return 대기(self.ctx)


class FailRound(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_user_value(trigger_id=900001, key='StartRound9', value=3)
            return 대기(self.ctx)


initial_state = 대기
