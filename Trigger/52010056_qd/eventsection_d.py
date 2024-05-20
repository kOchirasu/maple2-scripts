""" trigger/52010056_qd/eventsection_d.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class Idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=2005, spawn_ids=[999]):
            return 연출준비(self.ctx)


class 연출준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.select_camera_path(path_ids=[4006], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 경비병_외침(self.ctx)


class 경비병_외침(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_npc_emotion_sequence(spawn_id=999, sequence_name='Attack_01_B')
        self.add_cinematic_talk(npc_id=11003816, msg='$52010056_QD__EventSection_D__0$', duration=3727)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3727):
            return 크림슨스피어_출동(self.ctx)

    def on_exit(self) -> None:
        self.spawn_monster(spawn_ids=[901]) # 크림슨 스피어: 29000386
        self.spawn_monster(spawn_ids=[902]) # 크림슨 스피어: 29000386
        self.spawn_monster(spawn_ids=[903]) # 크림슨 스피어: 29000386
        self.spawn_monster(spawn_ids=[904]) # 크림슨 스피어: 29000386
        self.spawn_monster(spawn_ids=[905]) # 크림슨 스피어: 29000386
        self.spawn_monster(spawn_ids=[906]) # 크림슨 스피어: 29000386
        self.spawn_monster(spawn_ids=[907]) # 크림슨 스피어: 29000386
        self.spawn_monster(spawn_ids=[908]) # 크림슨 스피어: 29000386
        self.spawn_monster(spawn_ids=[909]) # 크림슨 스피어: 29000386
        self.spawn_monster(spawn_ids=[910]) # 크림슨 스피어: 29000386
        self.spawn_monster(spawn_ids=[911]) # 크림슨 스피어: 29000386
        self.spawn_monster(spawn_ids=[912]) # 크림슨 스피어: 29000386
        self.spawn_monster(spawn_ids=[913]) # 크림슨 스피어: 29000386
        self.spawn_monster(spawn_ids=[914]) # 크림슨 스피어: 29000386
        self.spawn_monster(spawn_ids=[915]) # 크림슨 스피어: 29000386
        self.change_monster(from_spawn_id=999, to_spawn_id=901)


class 크림슨스피어_출동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4007], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolation_time=1.0)
        self.remove_buff(box_id=2001, skill_id=70000107)


initial_state = Idle
