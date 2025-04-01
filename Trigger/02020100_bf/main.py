""" trigger/02020100_bf/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.enable_spawn_point_pc(spawn_id=1)
        self.enable_spawn_point_pc(spawn_id=2)
        self.enable_spawn_point_pc(spawn_id=3)
        self.set_user_value(trigger_id=99990002, key='Seed1start', value=0)
        self.set_user_value(trigger_id=99990003, key='Seed2start', value=0)
        self.set_user_value(trigger_id=99990004, key='Seed3start', value=0)
        self.set_portal(portal_id=1)
        self.set_ladder(trigger_ids=[2001])
        self.set_ladder(trigger_ids=[2002])
        self.set_ladder(trigger_ids=[2003])
        self.set_ladder(trigger_ids=[2004])
        self.set_ladder(trigger_ids=[2005])
        self.set_ladder(trigger_ids=[2006])
        self.set_ladder(trigger_ids=[2007])
        self.set_mesh(trigger_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014])
        self.set_mesh(trigger_ids=[1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114], visible=True)
        self.set_mesh(trigger_ids=[1201,1202,1203,1204,1205,1206,1207,1208,1209,1210,1211,1212,1213,1214,1215,1216,1217,1218,1219,1220,1221,1222,1223,1224,1225,1226,1227,1228,1229,1230], visible=True)
        self.set_actor(trigger_id=1401, visible=True, initial_sequence='Interaction_lapentatree_A01_Off')
        self.set_actor(trigger_id=1402, visible=True, initial_sequence='Interaction_lapentatree_A01_Off')
        self.set_actor(trigger_id=1403, visible=True, initial_sequence='Interaction_lapentatree_A01_Off')
        self.set_actor(trigger_id=1404, visible=True, initial_sequence='Interaction_lapentatree_A01_Off')
        self.set_mesh(trigger_ids=[1301,1302,1303,1304])
        self.set_interact_object(trigger_ids=[10002109], state=0)
        self.set_interact_object(trigger_ids=[10002110], state=0)
        self.set_interact_object(trigger_ids=[10002111], state=0)
        self.set_interact_object(trigger_ids=[10002112], state=0)
        self.set_interact_object(trigger_ids=[10002113], state=0)
        self.set_interact_object(trigger_ids=[10002115], state=0)
        self.set_interact_object(trigger_ids=[10002116], state=0)
        self.set_interact_object(trigger_ids=[10002122], state=0)
        self.set_breakable(trigger_ids=[5001,5002,5003,5004,5005,5006,5007,5008,5009])
        self.set_breakable(trigger_ids=[5011,5012,5013,5014,5015,5016,5017,5018,5019])
        self.set_agent(trigger_ids=[9001], visible=True)
        self.set_agent(trigger_ids=[9002], visible=True)
        self.set_agent(trigger_ids=[9003], visible=True)
        self.set_agent(trigger_ids=[9004], visible=True)
        self.set_agent(trigger_ids=[9005], visible=True)
        self.set_agent(trigger_ids=[9006], visible=True)
        self.set_agent(trigger_ids=[9007], visible=True)
        self.set_agent(trigger_ids=[9008], visible=True)
        self.set_agent(trigger_ids=[9009], visible=True)
        self.set_agent(trigger_ids=[9010], visible=True)
        self.set_agent(trigger_ids=[9011], visible=True)
        self.set_agent(trigger_ids=[9012], visible=True)
        self.set_agent(trigger_ids=[9013], visible=True)
        self.set_agent(trigger_ids=[9014], visible=True)
        self.set_agent(trigger_ids=[9015], visible=True)
        self.set_agent(trigger_ids=[9016], visible=True)
        self.set_agent(trigger_ids=[9017], visible=True)
        self.set_agent(trigger_ids=[9018], visible=True)
        self.set_agent(trigger_ids=[9019], visible=True)
        self.set_agent(trigger_ids=[9020], visible=True)
        self.set_agent(trigger_ids=[9021], visible=True)
        self.set_agent(trigger_ids=[9022], visible=True)
        self.set_agent(trigger_ids=[9023], visible=True)
        self.set_agent(trigger_ids=[9024], visible=True)
        self.set_agent(trigger_ids=[9025], visible=True)
        self.set_agent(trigger_ids=[9026], visible=True)
        self.set_agent(trigger_ids=[9027], visible=True)
        self.set_agent(trigger_ids=[9028], visible=True)
        self.set_agent(trigger_ids=[9029], visible=True)
        self.set_agent(trigger_ids=[9030], visible=True)
        self.set_agent(trigger_ids=[9031], visible=True)
        self.set_agent(trigger_ids=[9032], visible=True)
        self.set_agent(trigger_ids=[9033], visible=True)
        self.set_agent(trigger_ids=[9034], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[901]):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[9001])
        self.set_agent(trigger_ids=[9002])
        self.set_agent(trigger_ids=[9003])
        self.set_agent(trigger_ids=[9004])
        self.set_agent(trigger_ids=[9005])
        self.set_mesh(trigger_ids=[1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114])
        self.spawn_monster(spawn_ids=[201], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[201]):
            return 씨앗체험(self.ctx)


class 씨앗체험(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[9006])
        self.set_agent(trigger_ids=[9007])
        self.set_agent(trigger_ids=[9008])
        self.set_agent(trigger_ids=[9009])
        self.set_mesh(trigger_ids=[1007,1008,1009,1010], visible=True, interval=250, fade=3.0)
        self.spawn_monster(spawn_ids=[202,203,204,205], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[202,203,204,205]):
            return 씨앗체험_씨앗들기(self.ctx)


class 씨앗체험_씨앗들기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02020100_BF__MAIN__0$', duration=5000)
        self.set_user_value(trigger_id=99990005, key='Seed0start', value=1)
        # self.set_interact_object(trigger_ids=[10002115], state=1)
        # self.set_mesh(trigger_ids=[1301], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        """
        if self.object_interacted(interact_ids=[10002115], state=0):
            return 씨앗체험_나무심기(self.ctx)
        """
        if self.user_value(key='Seed0interact') == 1:
            return 씨앗체험_나무심기(self.ctx)


class 씨앗체험_나무심기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_mesh(trigger_ids=[1301])
        self.set_interact_object(trigger_ids=[10002116], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002116], state=0):
            self.set_actor(trigger_id=1401, visible=True, initial_sequence='Interaction_lapentatree_A01_On')
            self.set_user_value(trigger_id=99990005, key='Seed0start', value=2)
            return 씨앗체험_끝(self.ctx)


class 씨앗체험_끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[9010])
        self.set_agent(trigger_ids=[9011])
        self.set_agent(trigger_ids=[9012])
        self.set_agent(trigger_ids=[9013])
        self.set_mesh(trigger_ids=[1011,1012,1013,1014], visible=True, interval=250, fade=3.0)
        self.spawn_monster(spawn_ids=[207,208,209], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[207,208,209]):
            return 사다리활성화(self.ctx)


class 사다리활성화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[2001], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[2002], visible=True, enable=True, fade=4)
        self.set_ladder(trigger_ids=[2003], visible=True, enable=True, fade=6)
        self.set_ladder(trigger_ids=[2004], visible=True, enable=True, fade=8)
        self.set_ladder(trigger_ids=[2005], visible=True, enable=True, fade=10)
        self.set_ladder(trigger_ids=[2006], visible=True, enable=True, fade=12)
        self.set_ladder(trigger_ids=[2007], visible=True, enable=True, fade=14)
        self.spawn_monster(spawn_ids=[210,211,212], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[210,211,212]):
            return 씨앗1_활성화(self.ctx)


class 씨앗1_활성화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.enable_spawn_point_pc(spawn_id=0)
        self.enable_spawn_point_pc(spawn_id=1, is_enable=True)
        self.set_user_value(trigger_id=99990002, key='Seed1start', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Seed1interact') == 1:
            return 씨앗1_전투(self.ctx)


class 씨앗1_전투(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[9014])
        self.set_agent(trigger_ids=[9015])
        self.set_agent(trigger_ids=[9016])
        self.set_agent(trigger_ids=[9017])
        self.set_agent(trigger_ids=[9018])
        self.spawn_monster(spawn_ids=[213,214,215,216], auto_target=False)
        self.set_mesh(trigger_ids=[1201,1202,1203,1204,1205,1206,1207,1208,1209,1210])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[213,214,215,216]):
            return 씨앗1_심기(self.ctx)


class 씨앗1_심기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[9019])
        self.set_agent(trigger_ids=[9020])
        self.set_agent(trigger_ids=[9021])
        self.set_agent(trigger_ids=[9022])
        self.set_mesh(trigger_ids=[1001,1002,1003,1004], visible=True, interval=250, fade=3.0)
        self.set_interact_object(trigger_ids=[10002112], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002112], state=0):
            return 씨앗2_활성화(self.ctx)


class 씨앗2_활성화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[9023])
        self.set_agent(trigger_ids=[9024])
        self.enable_spawn_point_pc(spawn_id=1)
        self.enable_spawn_point_pc(spawn_id=2, is_enable=True)
        self.set_user_value(trigger_id=99990002, key='Seed1start', value=2)
        self.set_user_value(trigger_id=99990003, key='Seed2start', value=1)
        self.set_mesh(trigger_ids=[1005,1006], visible=True, interval=250, fade=3.0)
        self.set_actor(trigger_id=1402, visible=True, initial_sequence='Interaction_lapentatree_A01_On')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Seed2interact') == 1:
            return 씨앗2_전투(self.ctx)


class 씨앗2_전투(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[9025])
        self.set_agent(trigger_ids=[9026])
        self.set_agent(trigger_ids=[9027])
        self.set_agent(trigger_ids=[9028])
        self.set_agent(trigger_ids=[9029])
        self.set_event_ui_script(type=BannerType.Text, script='$02020100_BF__MAIN__1$', duration=5000)
        self.spawn_monster(spawn_ids=[111,112,113,114,115,116], auto_target=False)
        self.set_mesh(trigger_ids=[1211,1212,1213,1214,1215,1216,1217,1218,1219,1220])
        self.set_interact_object(trigger_ids=[10002113], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002113], state=0):
            return 발판1_지역감지(self.ctx)


class 발판1_지역감지(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[9030])
        self.set_agent(trigger_ids=[9031])
        self.set_agent(trigger_ids=[9032])
        self.set_agent(trigger_ids=[9033])
        self.set_agent(trigger_ids=[9034])
        self.set_actor(trigger_id=1403, visible=True, initial_sequence='Interaction_lapentatree_A01_On')
        self.set_mesh(trigger_ids=[1221,1222,1223,1224,1225,1226,1227,1228,1229,1230])
        self.destroy_monster(spawn_ids=[111,112,113,114,115,116])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[903]):
            return 발판1_활성화대기(self.ctx)


class 발판1_활성화대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[225,226], auto_target=False)
        self.set_user_value(trigger_id=99990003, key='Seed2start', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Seed3interact') == 1:
            return 발판1_몬스터처리(self.ctx)
        if self.monster_dead(spawn_ids=[225,226]):
            return 발판1_몬스터처리(self.ctx)


class 발판1_몬스터처리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99990004, key='Seed3start', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Seed3interact') == 1:
            return 발판1_활성화(self.ctx)


class 발판1_활성화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10002122], state=1)
        self.enable_spawn_point_pc(spawn_id=2)
        self.enable_spawn_point_pc(spawn_id=3, is_enable=True)
        self.spawn_monster(spawn_ids=[121,122,123,124], auto_target=False)
        self.set_breakable(trigger_ids=[5001,5002,5003,5004,5005,5006,5007,5008,5009], enable=True)
        self.set_breakable(trigger_ids=[5011,5012,5013,5014,5015,5016,5017,5018,5019], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='EliteClear') == 1:
            return 보스전(self.ctx)


class 보스전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99990005, key='Seed4start', value=2)
        self.destroy_monster(spawn_ids=[111,112,113,114,115,116,117,118,119])
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)


initial_state = 대기
