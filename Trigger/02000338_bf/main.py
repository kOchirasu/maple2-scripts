""" trigger/02000338_bf/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[120])
        self.set_ladder(trigger_ids=[121])
        self.set_ladder(trigger_ids=[122])
        self.set_ladder(trigger_ids=[123])
        self.set_ladder(trigger_ids=[124])
        self.set_ladder(trigger_ids=[110])
        self.set_ladder(trigger_ids=[111])
        self.set_ladder(trigger_ids=[112])
        self.set_mesh(trigger_ids=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])
        self.set_mesh(trigger_ids=[20,21,22,23,24,25,26,27,28,29,30,31,32])
        self.set_mesh(trigger_ids=[30001,30002,30003,30004,30005,30006,30007,30008,30009,30010,30011,30012,30013,30014,30015,30016,30017,30018,30019,30020,30021,30022,30023,30024,30025,30026,30027,30028,30029,30030,30031,30032,30033,30034], visible=True)
        self.set_mesh(trigger_ids=[20000,20001,20002,20003,20004,20005,20006,20007,20008,20009,20010,20011,20012,20013,20014,20015,20016,20017,20018,20019,20020,20021,20022,20023,20024,20025,20026,20027,20028,20029,20030,20031,20032,20033,20034,20035,20036,20037,20038,20039,20040,20041,20042,20043,20044,20045,20046,20047,20048,20049,20050,20051,20052,20053,20054,20055,20056,20057,20058,20059,20060,20061,20062,20063,20064,20065,20066,20067,20068,20069,20070,20071,20072,20073,20074,20075,20076,20077,20078,20079,20080,20081,20082,20083,20084,20085,20086,20087,20088,20089,20090,20091,20092,20093,20094,20095,20096,20097,20098,20099,20100,20101,20102,20103,20104,20105,20106,20107,20108,20109,20110,20111,20112,20113,20114,20115,20116,20117,20118,20119,20120,20121,20122,20123,20124,20125,20126,20127,20128,20129,20130,20131,20132,20133,20134,20135,20136,20137,20138,20139,20140,20141,20142,20143,20144,20145,20146,20147,20148,20149,20150,20151,20152,20153,20154,20155,20156,20157,20158,20159,20160,20161,20162,20163,20164,20165,20166,20167,20168,20169,20170,20171,20172,20173,20174,20175,20176,20177,20178,20179,20180,20181,20182,20183,20184,20185,20186,20187,20188,20189,20190,20191,20192,20193,20194,20195,20196,20197,20198,20199,20200,20201,20202,20203,20204,20205,20206,20207,20208,20209,20210,20211,20212,20213,20214,20215,20216,20217,20218,20219,20220,20221,20222,20223,20224,20225,20226,20227,20228,20229,20230,20231,20232,20233,20234,20235,20236,20237,20238,20239,20240,20241,20242,20243,20244,20245,20246,20247], visible=True)
        self.set_effect(trigger_ids=[32000]) # Vibrate
        self.set_effect(trigger_ids=[32001]) # Vibrate
        self.set_effect(trigger_ids=[32002], visible=True) # monochrome
        self.set_effect(trigger_ids=[90000]) # monochrome
        self.set_effect(trigger_ids=[73001]) # DownArrow
        self.set_effect(trigger_ids=[73002]) # DownArrow
        self.set_effect(trigger_ids=[74500])
        self.set_effect(trigger_ids=[75000]) # GuideArrow
        self.set_effect(trigger_ids=[75001]) # GuideArrow
        self.set_effect(trigger_ids=[75002]) # GuideArrow
        self.set_effect(trigger_ids=[75003]) # GuideArrow
        self.set_effect(trigger_ids=[75004]) # GuideArrow
        self.set_effect(trigger_ids=[75005]) # GuideArrow
        self.set_effect(trigger_ids=[76000]) # GuideArrow
        self.set_effect(trigger_ids=[76001]) # GuideArrow
        self.set_effect(trigger_ids=[76002]) # GuideArrow
        self.set_effect(trigger_ids=[73004])
        self.set_effect(trigger_ids=[73005])
        self.set_effect(trigger_ids=[73006])
        self.set_effect(trigger_ids=[73007])
        self.set_effect(trigger_ids=[74512])
        self.destroy_monster(spawn_ids=[5000])
        self.destroy_monster(spawn_ids=[5001,5002,5003,5004,5005,5006,5007,5008,5009,5010])
        self.set_interact_object(trigger_ids=[10000777], state=0)
        self.set_interact_object(trigger_ids=[10000778], state=0)
        self.set_interact_object(trigger_ids=[10000779], state=0)
        self.set_interact_object(trigger_ids=[10000780], state=0)
        self.set_interact_object(trigger_ids=[10000781], state=0)
        self.set_interact_object(trigger_ids=[10000782], state=0)
        self.spawn_monster(spawn_ids=[5101,5102,5103,5104,5105,5106,5107,5108,5109], auto_target=False)
        self.set_mesh(trigger_ids=[33,34,35,36,37,38,39,40,41])
        self.set_mesh(trigger_ids=[42,43,44,45,46,47,48])
        self.set_mesh(trigger_ids=[49,50,51,52,53,54,55])
        self.set_mesh(trigger_ids=[56,57,58,59,60,61,62,63,64,65,66])
        self.destroy_monster(spawn_ids=[5100])
        self.destroy_monster(spawn_ids=[5101,5102,5103,5104,5105,5106,5107,5108,5109,5110,5111,5112,5113,5114,5115,5116,5117,5118,5119,5120,5121,5122,5123,5124,5125])
        self.set_mesh(trigger_ids=[70001,70002,70003,70004,70005,70006,70007,70008,70009,70010])
        self.set_portal(portal_id=2)
        self.set_agent(trigger_ids=[8000], visible=True)
        self.set_agent(trigger_ids=[8001], visible=True)
        self.set_agent(trigger_ids=[8002], visible=True)
        self.set_agent(trigger_ids=[8003], visible=True)
        self.set_agent(trigger_ids=[8004], visible=True)
        self.set_agent(trigger_ids=[8005], visible=True)
        self.set_agent(trigger_ids=[8006], visible=True)
        self.set_agent(trigger_ids=[8007], visible=True)
        self.set_agent(trigger_ids=[8008], visible=True)
        self.set_agent(trigger_ids=[8009], visible=True)
        self.set_agent(trigger_ids=[8010], visible=True)
        self.set_agent(trigger_ids=[8011], visible=True)
        self.set_agent(trigger_ids=[8012], visible=True)
        self.set_agent(trigger_ids=[8013], visible=True)
        self.set_agent(trigger_ids=[8014], visible=True)
        self.set_agent(trigger_ids=[8015], visible=True)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return LoadingDelay(self.ctx)


class LoadingDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return DungeonStart(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.spawn_monster(spawn_ids=[5100], auto_target=False)
        self.set_mesh(trigger_ids=[70001,70002,70003,70004,70005,70006,70007,70008,70009], visible=True, start_delay=200, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[70010], visible=True, start_delay=250, interval=50, fade=2.0)
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraWalk01(self.ctx)


class CameraWalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_effect(trigger_ids=[74512], visible=True)
        self.select_camera(trigger_id=30200)
        self.set_skip(state=CameraWalk05)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return CameraWalk03(self.ctx)


class CameraWalk03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=30201)
        self.set_skip(state=CameraWalk05)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return CameraWalk04(self.ctx)


class CameraWalk04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_effect(trigger_ids=[74500], visible=True)
        self.set_skip(state=CameraWalk05)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return CameraWalk05(self.ctx)


class CameraWalk05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[5000], auto_target=False)
        self.move_npc(spawn_id=5000, patrol_name='MS2PatrolData5000')
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return GroundFall01(self.ctx)


class GroundFall01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[32000], visible=True)
        self.set_effect(trigger_ids=[32001], visible=True)
        self.set_mesh(trigger_ids=[20000,20001,20002,20003,20004,20005,20006,20007,20008,20009,20010,20011,20012,20013,20014,20015,20016,20017,20018,20019,20020], start_delay=100)
        self.set_mesh(trigger_ids=[20233,20234,20235,20236,20237,20238,20239,20240,20241,20242,20243,20244,20245,20246,20247], start_delay=100, fade=50.0)
        self.set_mesh(trigger_ids=[20226,20227,20228,20229,20230,20231], start_delay=100)
        self.set_mesh(trigger_ids=[30001,30002,30003,30004,30005,30006,30007,30008,30009,30010,30011,30012,30013,30014,30015,30016,30017,30018,30019,30020,30021,30022,30023,30024,30025,30026,30027,30028,30029,30030,30031,30032,30033,30034], start_delay=200)
        self.set_mesh(trigger_ids=[20021,20022,20023,20024,20025,20026,20027,20028], start_delay=250, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[20029,20030,20031,20032,20033,20034,20035,20036], start_delay=500, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[20037,20038,20039,20040,20041,20042,20043,20044,20045,20046,20047,20048,20049,20050], start_delay=750, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[20051,20052,20053,20054,20055,20056,20057,20058,20059,20060,20061,20062,20063,20064], start_delay=1000, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[20065,20066,20067,20068,20069,20070,20071,20072,20073,20074,20075,20076,20077,20078,20079,20080], start_delay=1250, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[20081,20082,20083,20084,20085,20086,20087,20088,20089,20090,20091,20092,20093], start_delay=1500, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[20094,20095,20096,20097,20098,20099,20100,20101,20102,20103,20104,20105,20106], start_delay=1500, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[20107,20108,20109,20110,20111,20112,20113,20114,20115], start_delay=1750, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[20116,20117,20118,20119,20120,20121,20122,20123], start_delay=2000, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[20124,20125,20126,20127,20128,20129], start_delay=2250, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[20130,20131,20132,20133,20134,20135], start_delay=2500, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[20136,20137,20138,20139,20140,20141,20142,20143], start_delay=2750, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[20144,20145,20146,20147,20148,20149,20150,20151,20152], start_delay=3000, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[20153,20154,20155,20156,20157], start_delay=3250, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[20158,20159,20160,20161,20162,20163,20164,20165,20166,20167,20168,20169], start_delay=3500, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[20232], start_delay=3500, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[20170,20171,20172,20173,20174,20175,20176,20177,20178,20179,20180,20181,20182,20183,20184], start_delay=3750, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[20185,20186,20187,20188,20189,20190,20191,20192,20193,20194,20195,20196,20197,20198], start_delay=4000, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[20199,20200,20201,20202,20203,20204,20205,20206,20207,20208,20209,20210], start_delay=4250, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[20211,20212,20213,20214,20215,20216], start_delay=4500, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[20217,20218,20219], start_delay=4750, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[20220,20221,20222,20223,20224,20225], start_delay=5000, interval=50, fade=2.0)
        self.set_skip(state=차어나운스3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 차어나운스3(self.ctx)


class 차어나운스3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State
        self.reset_camera(interpolation_time=1.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Ready01(self.ctx)


class Ready01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_mesh(trigger_ids=[70001,70002,70003,70004,70005,70006,70007,70008,70009,70010])
        self.set_portal(portal_id=2)
        self.set_effect(trigger_ids=[75000], visible=True) # GuideArrow
        self.set_effect(trigger_ids=[75001], visible=True) # GuideArrow
        self.set_effect(trigger_ids=[75002], visible=True) # GuideArrow
        self.set_effect(trigger_ids=[75003], visible=True) # GuideArrow
        self.set_effect(trigger_ids=[75004], visible=True) # GuideArrow
        self.set_effect(trigger_ids=[75005], visible=True) # GuideArrow
        self.set_mesh(trigger_ids=[20000,20001,20002,20003,20004,20005,20006,20007,20008,20009,20010,20011,20012,20013,20014,20015,20016,20017,20018,20019,20020])
        self.set_mesh(trigger_ids=[20233,20234,20235,20236,20237,20238,20239,20240,20241,20242,20243,20244,20245,20246,20247])
        self.set_mesh(trigger_ids=[20226,20227,20228,20229,20230,20231])
        self.set_mesh(trigger_ids=[30001,30002,30003,30004,30005,30006,30007,30008,30009,30010,30011,30012,30013,30014,30015,30016,30017,30018,30019,30020,30021,30022,30023,30024,30025,30026,30027,30028,30029,30030,30031,30032,30033,30034])
        self.set_mesh(trigger_ids=[20021,20022,20023,20024,20025,20026,20027,20028])
        self.set_mesh(trigger_ids=[20029,20030,20031,20032,20033,20034,20035,20036])
        self.set_mesh(trigger_ids=[20037,20038,20039,20040,20041,20042,20043,20044,20045,20046,20047,20048,20049,20050])
        self.set_mesh(trigger_ids=[20051,20052,20053,20054,20055,20056,20057,20058,20059,20060,20061,20062,20063,20064])
        self.set_mesh(trigger_ids=[20065,20066,20067,20068,20069,20070,20071,20072,20073,20074,20075,20076,20077,20078,20079,20080])
        self.set_mesh(trigger_ids=[20081,20082,20083,20084,20085,20086,20087,20088,20089,20090,20091,20092,20093])
        self.set_mesh(trigger_ids=[20094,20095,20096,20097,20098,20099,20100,20101,20102,20103,20104,20105,20106])
        self.set_mesh(trigger_ids=[20107,20108,20109,20110,20111,20112,20113,20114,20115])
        self.set_mesh(trigger_ids=[20116,20117,20118,20119,20120,20121,20122,20123])
        self.set_mesh(trigger_ids=[20124,20125,20126,20127,20128,20129])
        self.set_mesh(trigger_ids=[20130,20131,20132,20133,20134,20135])
        self.set_mesh(trigger_ids=[20136,20137,20138,20139,20140,20141,20142,20143])
        self.set_mesh(trigger_ids=[20144,20145,20146,20147,20148,20149,20150,20151,20152])
        self.set_mesh(trigger_ids=[20153,20154,20155,20156,20157])
        self.set_mesh(trigger_ids=[20158,20159,20160,20161,20162,20163,20164,20165,20166,20167,20168,20169])
        self.set_mesh(trigger_ids=[20232])
        self.set_mesh(trigger_ids=[20170,20171,20172,20173,20174,20175,20176,20177,20178,20179,20180,20181,20182,20183,20184])
        self.set_mesh(trigger_ids=[20185,20186,20187,20188,20189,20190,20191,20192,20193,20194,20195,20196,20197,20198])
        self.set_mesh(trigger_ids=[20199,20200,20201,20202,20203,20204,20205,20206,20207,20208,20209,20210])
        self.set_mesh(trigger_ids=[20211,20212,20213,20214,20215,20216])
        self.set_mesh(trigger_ids=[20217,20218,20219])
        self.set_mesh(trigger_ids=[20220,20221,20222,20223,20224,20225])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return FirstBattle01(self.ctx)


class FirstBattle01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[102], sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20003382, text_id=20003382)
        self.spawn_monster(spawn_ids=[5001,5002,5003], auto_target=False)
        self.set_effect(trigger_ids=[73001], visible=True)
        self.set_interact_object(trigger_ids=[10000777], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000777], state=0):
            return FirstBridgeOn01(self.ctx)


class FirstBridgeOn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[75000]) # GuideArrow
        self.set_effect(trigger_ids=[75001]) # GuideArrow
        self.set_effect(trigger_ids=[75002]) # GuideArrow
        self.set_effect(trigger_ids=[75003]) # GuideArrow
        self.set_effect(trigger_ids=[75004]) # GuideArrow
        self.set_effect(trigger_ids=[75005]) # GuideArrow
        self.set_agent(trigger_ids=[8000])
        self.set_agent(trigger_ids=[8001])
        self.set_agent(trigger_ids=[8002])
        self.hide_guide_summary(entity_id=20003382)
        self.set_effect(trigger_ids=[73001])
        self.set_mesh(trigger_ids=[20,21,22,23,24,25,26,27,28,29,30,31,32], visible=True, start_delay=100, interval=50, fade=2.0)
        self.spawn_monster(spawn_ids=[5004,5005,5006,5007,5008,5009,5010], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return SecondBattle01(self.ctx)


class SecondBattle01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[102], sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20003382, text_id=20003382)
        self.set_interact_object(trigger_ids=[10000778], state=1)
        self.set_effect(trigger_ids=[73002], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000778], state=0):
            return SecondBridgeOn01(self.ctx)


class SecondBridgeOn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[8003])
        self.set_agent(trigger_ids=[8004])
        self.set_agent(trigger_ids=[8005])
        self.hide_guide_summary(entity_id=20003382)
        self.show_guide_summary(entity_id=20003386, text_id=20003386, duration=5000)
        self.play_system_sound_in_box(box_ids=[102], sound='System_ShowGuideSummary_01')
        self.set_effect(trigger_ids=[73002])
        self.set_mesh(trigger_ids=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19], visible=True, start_delay=100, interval=50, fade=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[5000]):
            return ThirdBattle01(self.ctx)


class ThirdBattle01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[76000], visible=True) # GuideArrow
        self.set_effect(trigger_ids=[76001], visible=True) # GuideArrow
        self.set_effect(trigger_ids=[76002], visible=True) # GuideArrow
        self.set_ladder(trigger_ids=[120], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[121], visible=True, enable=True, fade=4)
        self.set_ladder(trigger_ids=[122], visible=True, enable=True, fade=6)
        self.set_ladder(trigger_ids=[123], visible=True, enable=True, fade=8)
        self.set_ladder(trigger_ids=[124], visible=True, enable=True, fade=10)
        self.set_ladder(trigger_ids=[110], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[111], visible=True, enable=True, fade=4)
        self.set_ladder(trigger_ids=[112], visible=True, enable=True, fade=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[999998]):
            return ThirdBrigeOn01(self.ctx)


class ThirdBrigeOn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[76000]) # GuideArrow
        self.set_effect(trigger_ids=[76001]) # GuideArrow
        self.set_effect(trigger_ids=[76002]) # GuideArrow

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FourthBattle01(self.ctx)


class FourthBattle01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[102], sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20003382, text_id=20003382)
        self.set_interact_object(trigger_ids=[10000779], state=1)
        self.set_effect(trigger_ids=[73004], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000779], state=0):
            return FourthBridgeOn01(self.ctx)


class FourthBridgeOn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=20003382)
        self.set_effect(trigger_ids=[73004])
        self.set_mesh(trigger_ids=[33,34,35,36,37,38,39,40,41], visible=True, start_delay=100, interval=50, fade=2.0)
        self.spawn_monster(spawn_ids=[5110,5111,5112,5113,5114,5115,5116,5117,5118,5119,5120,5121], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return FifthBattle01(self.ctx)


class FifthBattle01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[102], sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20003382, text_id=20003382)
        self.set_interact_object(trigger_ids=[10000780], state=1)
        self.set_effect(trigger_ids=[73005], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000780], state=0):
            return FifthBridgeOn01(self.ctx)


class FifthBridgeOn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[8006])
        self.set_agent(trigger_ids=[8007])
        self.set_agent(trigger_ids=[8008])
        self.hide_guide_summary(entity_id=20003382)
        self.set_effect(trigger_ids=[73005])
        self.set_mesh(trigger_ids=[42,43,44,45,46,47,48], visible=True, start_delay=100, interval=50, fade=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return SixthBattle01(self.ctx)


class SixthBattle01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[102], sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20003382, text_id=20003382)
        self.set_interact_object(trigger_ids=[10000781], state=1)
        self.set_effect(trigger_ids=[73006], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000781], state=0):
            return SixthBridgeOn01(self.ctx)


class SixthBridgeOn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[8009])
        self.set_agent(trigger_ids=[8010])
        self.hide_guide_summary(entity_id=20003382)
        self.set_effect(trigger_ids=[73006])
        self.set_mesh(trigger_ids=[49,50,51,52,53,54,55], visible=True, start_delay=100, interval=50, fade=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return SeventhBattle01(self.ctx)


class SeventhBattle01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[102], sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20003382, text_id=20003382)
        self.set_interact_object(trigger_ids=[10000782], state=1)
        self.set_effect(trigger_ids=[73007], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000782], state=0):
            return SeventhBridgeOn01(self.ctx)


# 보스 전투 돌입
class SeventhBridgeOn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[8011])
        self.set_agent(trigger_ids=[8012])
        self.set_agent(trigger_ids=[8013])
        self.set_agent(trigger_ids=[8014])
        self.set_agent(trigger_ids=[8015])
        self.hide_guide_summary(entity_id=20003382)
        self.set_mesh(trigger_ids=[56,57,58,59,60,61,62,63,64,65,66], visible=True, start_delay=100, interval=50, fade=2.0)
        self.play_system_sound_in_box(box_ids=[102], sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20003381, text_id=20003381, duration=7000)
        self.set_effect(trigger_ids=[73007])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[5100]):
            return BossBattle01(self.ctx)


class BossBattle01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear()
        self.set_mesh(trigger_ids=[70001,70002,70003,70004,70005,70006,70007,70008,70009], visible=True, start_delay=200, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[70010], visible=True, start_delay=250, interval=50, fade=2.0)
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=20000):
            return PCGetOut01(self.ctx)


class PCGetOut01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            return PCGetOut02(self.ctx)


class PCGetOut02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            return PCGetOut03(self.ctx)


class PCGetOut03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            return PCGetOut04(self.ctx)


class PCGetOut04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user()


initial_state = 대기
