""" trigger/02020025_bf/02020025_battle.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='Success', value=0)
        self.set_user_value(trigger_id=99999001, key='End', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='battlesetting') == 1:
            return 전투_시작(self.ctx)


class 전투_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_reset_time(seconds=300)
        self.set_npc_duel_hp_bar(is_open=True, spawn_id=201, duration_tick=300000, npc_hp_step=100)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_play_time() <= 180 and self.monster_dead(spawn_ids=[201]):
            # <한국용 컨디션체크>
            self.dungeon_mission_complete(mission_id=24092005)
            return 전투_종료(self.ctx)
        if self.dungeon_play_time() <= 70 and self.monster_dead(spawn_ids=[201]):
            # <중국용 컨디션체크>
            self.dungeon_mission_complete(mission_id=24092006)
            return 전투_종료(self.ctx)
        if self.dungeon_play_time() <= 270 and self.monster_dead(spawn_ids=[201]):
            # <NA용 컨디션체크>
            self.dungeon_mission_complete(mission_id=24092010)
            return 전투_종료(self.ctx)
        if self.monster_dead(spawn_ids=[201]):
            # <5분내에 처치>
            return 전투_종료(self.ctx)
        if not self.user_detected(box_ids=[902]):
            # <pc 사망>
            return 전투_종료(self.ctx)
        if self.dungeon_play_time() >= 300:
            # <5분 다 지날 경우>
            return 전투_종료(self.ctx)


class 전투_종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_set_end_time()
        self.destroy_monster(spawn_ids=[-1])
        # self.add_buff(box_ids=[902], skill_id=72000050, level=1)
        # self.set_npc_emotion_loop(spawn_id=201, sequence_name='Attack_Idle_A', duration=60000.0)
        self.side_npc_talk(npc_id=24110001, illust='Conder_normal', duration=4000, script='$02020025_BF__02020025_battle__0$', voice='ko/Npc/00002258')
        self.set_npc_duel_hp_bar(spawn_id=201)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 종료신호(self.ctx)


class 종료신호(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99999001, key='End', value=1)


initial_state = 대기
