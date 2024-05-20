""" trigger/52010038_qd/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=11)
        self.set_effect(trigger_ids=[6299])
        self.shadow_expedition_close_boss_gauge()
        self.set_mesh(trigger_ids=[3000,3001,3002,3003,3004,3005], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199]):
            return 준비(self.ctx)


class 준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.add_buff(box_ids=[199], skill_id=70000109, level=1, is_player=False, is_skill_set=False)
        self.spawn_monster(spawn_ids=[1805,1806], auto_target=False)
        self.spawn_monster(spawn_ids=[1201], auto_target=False)
        self.spawn_npc_range(range_ids=[1001,1002,1003,1004,1005,1006,1007,1008])
        self.spawn_npc_range(range_ids=[1101,1102,1103,1104,1105,1106])
        self.spawn_npc_range(range_ids=[1801,1802,1803,1804])
        # self.set_cinematic_intro(text='<font color=\'#ffd200\' size=\'90\'>Press \'ESC\' to Start</font>\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n')
        self.set_skip(state=시작)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 시작(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State
        self.set_user_value(trigger_id=999001, key='GaugeOpen', value=1)
        self.set_user_value(trigger_id=992001, key='WaveStart', value=1)
        self.set_user_value(trigger_id=999004, key='AllertStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.shadow_expedition_points() >= 150:
            return 부상병발생(self.ctx)


class 부상병발생(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11003533, illust='Bliche_nomal', duration=7000, script='$52010038_QD__main__4$', voice='ko/Npc/00002057')
        self.set_user_value(trigger_id=993001, key='WoundStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.shadow_expedition_points() >= 300:
            return 차폭탄방어2(self.ctx)


class 차폭탄방어2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=60, start_delay=1, interval=1, v_offset=80)
        self.set_user_value(trigger_id=992003, key='bombStart', value=1)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_skip(state=연출02종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 카메라304(self.ctx)


class 카메라304(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=304)
        self.set_skip(state=연출02종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 부관대사03(self.ctx)


class 부관대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip(state=연출02종료)
        self.add_cinematic_talk(npc_id=11003536, illust_id='Neirin_surprise', msg='$52010038_QD__MAIN__0$', duration=7000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 연출02종료(self.ctx)


class 연출02종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera()
        self.set_skip() # Missing State: State
        self.side_npc_talk(npc_id=11003537, illust='Mason_closeEye', duration=7000, script='$52010038_QD__main__5$', voice='ko/Npc/00002095')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2008,2009,2010]):
            self.spawn_monster(spawn_ids=[4020], auto_target=False)
            self.spawn_monster(spawn_ids=[4020], auto_target=False)
            self.reset_timer(timer_id='99')
            return 차폭탄방어완료조건2(self.ctx)


class 차폭탄방어완료조건2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2097]):
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=1000):
            self.side_npc_talk(npc_id=11003536, illust='Neirin_normal', duration=6000, script='$52010038_QD__main__6$', voice='ko/Npc/00002106')
            return 층이벤트스킵3(self.ctx)


class 층이벤트스킵3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.shadow_expedition_points() >= 700:
            return 보스등장(self.ctx)


class 보스등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6201,6202,6203,6204])
        self.spawn_monster(spawn_ids=[2098], auto_target=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_skip(state=보스연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 카메라302(self.ctx)


class 카메라302(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=302)
        self.set_skip(state=보스연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 보스대사01(self.ctx)


class 보스대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip(state=보스연출종료)
        self.add_cinematic_talk(npc_id=11003185, illust_id='ShadowClaw_normal', msg='$52010038_QD__MAIN__2$', duration=5000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 보스이동(self.ctx)


class 보스이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip(state=보스연출종료)
        self.move_npc(spawn_id=2098, patrol_name='MS2PatrolData_2098')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 카메라303(self.ctx)


class 카메라303(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003185, illust_id='ShadowClaw_normal', msg='$52010038_QD__MAIN__3$', duration=5000, align=Align.Left)
        self.select_camera(trigger_id=303)
        self.set_skip(state=보스연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 보스연출종료(self.ctx)


class 보스연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6299], visible=True)
        self.side_npc_talk(npc_id=11003533, illust='Bliche_nomal', duration=7000, script='$52010038_QD__main__8$', voice='ko/Npc/00002058')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera()
        self.set_skip() # Missing State: State
        self.destroy_monster(spawn_ids=[2098])
        self.spawn_monster(spawn_ids=[2099])
        self.spawn_monster(spawn_ids=[1099], auto_target=False)
        self.set_user_value(trigger_id=992001, key='WaveSlowDown', value=1)
        self.set_user_value(trigger_id=992002, key='WaveStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.shadow_expedition_points() >= 1000:
            return 종료(self.ctx)
        if self.monster_dead(spawn_ids=[1099]):
            self.set_user_value(trigger_id=999001, key='EngineIsDead', value=1)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
