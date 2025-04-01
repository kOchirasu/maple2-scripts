""" trigger/80000015_bonus/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6000])
        self.set_interact_object(trigger_ids=[10001339], state=1)
        self.set_interact_object(trigger_ids=[10001340], state=2)
        self.set_portal(portal_id=2)
        self.set_mesh(trigger_ids=[3020,3021,3022,3023], visible=True)
        self.set_mesh(trigger_ids=[3024])
        self.set_mesh(trigger_ids=[30001,30002,30003,30004,30005,30006,30007,30008,30009,30010,30011,30012,30013,30014,30015,30016,30017,30018,30019,30020,30021,30022,30023,30024,30025,30026,30027,30028,30029,30030,30031,30032,30033,30034,30035,30036,30037,30038,30039,30040,30041,30042,30043,30044,30045,30046,30047,30048,30049,30050,30051,30052,30053,30054,30055,30056,30057,30058,30059,30060,30061,30062,30063,30064,30065,30066,30067,30068,30069,30070,30071,30072,30073,30074,30075,30076,30077,30078,30079,30080,30081,30082,30083,30084,30085,30086,30087,30088,30089,30090], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199]):
            # self.set_timer(timer_id='30', seconds=600, auto_remove=True, display=True, v_offset=80)
            return 문열기(self.ctx)


class 문열기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001339], state=0):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.score_board_create(type='ScoreBoardTopCenter')
        self.score_board_set_score(score=0)
        self.spawn_item_range(range_ids=[9001,9002,9003,9004,9005,9006,9007,9008,9009,9010,9011,9012,9013,9014,9015,9016,9017,9018,9019], random_pick_count=11)
        self.set_event_ui_script(type=BannerType.Text, script='$80000015_bonus__main__0$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        """
        if self.wait_tick(wait_tick=1500):
            pass
        """
        if self.user_value(key='Dead_A') == 1 and self.user_value(key='Dead_B') == 1:
            return 보스소환대기(self.ctx)


class 보스소환대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[198]) and self.user_detected(box_ids=[194]):
            return 보스등장(self.ctx)


class 보스등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6000], visible=True)
        self.set_mesh(trigger_ids=[30001,30002,30003,30004,30005,30006,30007,30008,30009,30010,30011,30012,30013,30014,30015,30016,30017,30018,30019,30020,30021,30022,30023,30024,30025,30026,30027,30028,30029,30030,30031,30032,30033,30034,30035,30036,30037,30038,30039,30040,30041,30042,30043,30044,30045,30046,30047,30048,30049,30050,30051,30052,30053,30054,30055,30056,30057,30058,30059,30060,30061,30062,30063,30064,30065,30066,30067,30068,30069,30070,30071,30072,30073,30074,30075,30076,30077,30078,30079,30080,30081,30082,30083,30084,30085,30086,30087,30088,30089,30090], fade=3.0)
        self.spawn_npc_range(range_ids=[2099], score=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2099]):
            return 딜레이(self.ctx)


class 딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[0])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 정산(self.ctx)


class 정산(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3020,3021,3022,3023])
        self.set_mesh(trigger_ids=[3024], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.score_board_score() >= 28000:
            self.debug_string(value='28000 이상')
            # self.set_event_ui_script(type=BannerType.Success, script='미션 성공! 참 잘했어요!', duration=2500)
            self.set_achievement(trigger_id=199, type='trigger', achieve='HighScoreTreasureMap04')
            return 반응대기(self.ctx)
        if self.score_board_score() < 28000:
            self.debug_string(value='28000 미만')
            # self.set_event_ui_script(type=BannerType.Success, script='미션 성공!', duration=2500)
            return 반응대기(self.ctx)
        if self.wait_tick(wait_tick=500):
            return 반응대기(self.ctx)


class 반응대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001340], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001340], state=0):
            self.dungeon_clear()
            self.set_achievement(trigger_id=199, type='trigger', achieve='TreasureMap04')
            self.score_board_remove()
            self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
