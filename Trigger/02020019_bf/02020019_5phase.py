""" trigger/02020019_bf/02020019_5phase.xml """
import trigger_api


# <5페이즈 크림슨 발록의 AI 너프버전으로 시작>
class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='5Phase') == 1:
            return 크림슨발록스폰체크(self.ctx)


class 크림슨발록스폰체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(feature='FameChallengeBuff_01', box_ids=[241], skill_id=49218001, level=1) # <한국용 공격력 1.2배 강화 버프>
        self.add_buff(feature='FameChallengeBuff_01', box_ids=[242], skill_id=49218001, level=1)
        self.add_buff(feature='FameChallengeBuff_01', box_ids=[243], skill_id=49218001, level=1)
        self.add_buff(feature='FameChallengeBuff_01', box_ids=[244], skill_id=49218001, level=1)
        self.add_buff(feature='FameChallengeBuff_01', box_ids=[245], skill_id=49218001, level=1)
        self.add_buff(feature='FameChallengeBuff_01', box_ids=[246], skill_id=49218001, level=1)
        self.add_buff(feature='FameChallengeBuff_01', box_ids=[247], skill_id=49218001, level=1)
        self.add_buff(feature='FameChallengeBuff_02', box_ids=[241], skill_id=49218002, level=1) # <중국용 공격력 2배 강화 버프>
        self.add_buff(feature='FameChallengeBuff_02', box_ids=[242], skill_id=49218002, level=1)
        self.add_buff(feature='FameChallengeBuff_02', box_ids=[243], skill_id=49218002, level=1)
        self.add_buff(feature='FameChallengeBuff_02', box_ids=[244], skill_id=49218002, level=1)
        self.add_buff(feature='FameChallengeBuff_02', box_ids=[245], skill_id=49218002, level=1)
        self.add_buff(feature='FameChallengeBuff_02', box_ids=[246], skill_id=49218002, level=1)
        self.add_buff(feature='FameChallengeBuff_02', box_ids=[247], skill_id=49218002, level=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(spawn_ids=[242]):
            return 크림슨스피어죽음(self.ctx)


class 크림슨스피어죽음(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[241]):
            return 발록에게신호쏴주기(self.ctx)


class 발록에게신호쏴주기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ai_extra_data(key='SpearDead', value=1)


initial_state = 대기
