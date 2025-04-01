""" trigger/02020019_bf/02020019_battle.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[-1])
        self.set_user_value(trigger_id=99990004, key='TimerReset', value=0)
        self.set_user_value(key='Success', value=0)
        self.set_user_value(trigger_id=99990001, key='End', value=0)
        self.set_user_value(trigger_id=99990003, key='5Phase', value=0)
        self.debug_string(feature='Develop', value='이건 Develop 환경에서 나오는 스트링 입니다.')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='battlesetting') == 1:
            return 전투_1라운드세팅(self.ctx)


class 전투_1라운드세팅(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_reset_time(seconds=300)
        self.show_round_ui(round=1, duration=3000)
        self.set_event_ui_round(rounds=[1,5])
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_B', duration=4800.0)
        self.side_npc_talk(npc_id=24100001, illust='Neirin_normal', duration=5000, script='$02020019_BF__02020019_battle__0$', voice='ko/Npc/00002116')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 전투_1라운드시작(self.ctx)


class 전투_1라운드시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[201])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[201]):
            return 전투_1라운드종료(self.ctx)
        if not self.user_detected(box_ids=[901]):
            return 전투_종료(self.ctx)
        if self.dungeon_play_time() >= 300:
            return 전투_종료(self.ctx)


class 전투_1라운드종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_mission_complete(mission_id=24093001)
        self.destroy_monster(spawn_ids=[201])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 전투_2라운드세팅(self.ctx)
        if not self.user_detected(box_ids=[901]):
            return 전투_종료(self.ctx)
        if self.dungeon_play_time() >= 300:
            return 전투_종료(self.ctx)


class 전투_2라운드세팅(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_round_ui(round=2, duration=3000)
        self.set_event_ui_round(rounds=[2,5])
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_B', duration=4800.0)
        self.side_npc_talk(npc_id=24100001, illust='Neirin_normal', duration=5000, script='$02020019_BF__02020019_battle__1$', voice='ko/Npc/00002121')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 전투_2라운드시작(self.ctx)
        if not self.user_detected(box_ids=[901]):
            return 전투_종료(self.ctx)
        if self.dungeon_play_time() >= 300:
            return 전투_종료(self.ctx)


class 전투_2라운드시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[211])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[211]):
            return 전투_2라운드종료(self.ctx)
        if not self.user_detected(box_ids=[901]):
            return 전투_종료(self.ctx)
        if self.dungeon_play_time() >= 300:
            return 전투_종료(self.ctx)


class 전투_2라운드종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_mission_complete(mission_id=24093002)
        self.destroy_monster(spawn_ids=[211])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 전투_3라운드세팅(self.ctx)
        if not self.user_detected(box_ids=[901]):
            return 전투_종료(self.ctx)
        if self.dungeon_play_time() >= 300:
            return 전투_종료(self.ctx)


class 전투_3라운드세팅(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_round_ui(round=3, duration=3000)
        self.set_event_ui_round(rounds=[3,5])
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_B', duration=4800.0)
        self.side_npc_talk(npc_id=24100001, illust='Neirin_normal', duration=5000, script='$02020019_BF__02020019_battle__2$', voice='ko/Npc/00002241')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 전투_3라운드시작(self.ctx)
        if not self.user_detected(box_ids=[901]):
            return 전투_종료(self.ctx)
        if self.dungeon_play_time() >= 300:
            return 전투_종료(self.ctx)


class 전투_3라운드시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[221,222,223,224,225,226,227])

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_hp(spawn_id=221, is_relative=True) <= 50:
            return 전투_3라운드버프(self.ctx)
        if not self.user_detected(box_ids=[901]):
            return 전투_종료(self.ctx)
        if self.dungeon_play_time() >= 300:
            return 전투_종료(self.ctx)


class 전투_3라운드버프(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=24100001, illust='Neirin_serious', duration=5000, script='$02020019_BF__02020019_battle__3$', voice='ko/Npc/00002117')
        self.add_buff(box_ids=[221], skill_id=49219001, level=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[221,222,223,224,225,226,227]):
            return 전투_3라운드종료(self.ctx)
        if not self.user_detected(box_ids=[901]):
            return 전투_종료(self.ctx)
        if self.dungeon_play_time() >= 300:
            return 전투_종료(self.ctx)


class 전투_3라운드종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[221,222,223,224,225,226,227])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 전투_4라운드세팅(self.ctx)
        if not self.user_detected(box_ids=[901]):
            return 전투_종료(self.ctx)
        if self.dungeon_play_time() >= 300:
            return 전투_종료(self.ctx)


class 전투_4라운드세팅(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_round_ui(round=4, duration=3000)
        self.set_event_ui_round(rounds=[4,5])
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_B', duration=4800.0)
        self.side_npc_talk(npc_id=24100001, illust='Neirin_normal', duration=5000, script='$02020019_BF__02020019_battle__4$', voice='ko/Npc/00002242')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 전투_4라운드시작(self.ctx)
        if not self.user_detected(box_ids=[901]):
            return 전투_종료(self.ctx)
        if self.dungeon_play_time() >= 300:
            return 전투_종료(self.ctx)


class 전투_4라운드시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[231,232,233,234,235,236,237])
        self.side_npc_talk(npc_id=24100001, illust='Neirin_normal', duration=5000, script='$02020019_BF__02020019_battle__5$', voice='ko/Npc/00002243')
        self.set_ai_extra_data(key='Autofire', value=1) # <대포 쏘기 시작 AI에 신호쏴주기>

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_hp(spawn_id=231, is_relative=True) <= 50:
            return 전투_4라운드버프(self.ctx)
        if not self.user_detected(box_ids=[901]):
            return 전투_종료(self.ctx)
        if self.dungeon_play_time() >= 300:
            return 전투_종료(self.ctx)


class 전투_4라운드버프(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=24100001, illust='Neirin_serious', duration=5000, script='$02020019_BF__02020019_battle__6$', voice='ko/Npc/00002118')
        self.add_buff(box_ids=[231], skill_id=49219001, level=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[231,232,233,234,235,236,237]):
            return 전투_4라운드종료(self.ctx)
        if not self.user_detected(box_ids=[901]):
            return 전투_종료(self.ctx)
        if self.dungeon_play_time() >= 300:
            return 전투_종료(self.ctx)


class 전투_4라운드종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_mission_complete(mission_id=24093003)
        self.destroy_monster(spawn_ids=[231,232,233,234,235,236,237])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 전투_5라운드세팅(self.ctx)
        if not self.user_detected(box_ids=[901]):
            return 전투_종료(self.ctx)
        if self.dungeon_play_time() >= 300:
            return 전투_종료(self.ctx)


class 전투_5라운드세팅(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_round_ui(round=5, duration=3000)
        self.set_event_ui_round(rounds=[5,5])
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_B', duration=4800.0)
        self.side_npc_talk(npc_id=24100001, illust='Neirin_normal', duration=5000, script='$02020019_BF__02020019_battle__7$', voice='ko/Npc/00002122')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_user_value(trigger_id=99990003, key='5Phase', value=1)
            return 전투_5라운드시작(self.ctx)
        if not self.user_detected(box_ids=[901]):
            return 전투_종료(self.ctx)
        if self.dungeon_play_time() >= 300:
            return 전투_종료(self.ctx)


class 전투_5라운드시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[241,242,243,244,245,246,247,248])

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_hp(spawn_id=241, is_relative=True) <= 50:
            return 전투_5라운드버프(self.ctx)
        if self.npc_hp(spawn_id=242, is_relative=True) <= 50:
            return 전투_5라운드버프(self.ctx)
        if not self.user_detected(box_ids=[901]):
            return 전투_종료(self.ctx)
        if self.dungeon_play_time() >= 300:
            return 전투_종료(self.ctx)


class 전투_5라운드버프(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=24100001, illust='Neirin_serious', duration=5000, script='$02020019_BF__02020019_battle__8$', voice='ko/Npc/00002119')
        self.add_buff(box_ids=[241], skill_id=49219001, level=1)
        self.add_buff(box_ids=[242], skill_id=49219001, level=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_play_time() <= 180 and self.monster_dead(spawn_ids=[241,242,243,244,245,246,247,248]):
            # <한국용 컨디션체크>
            self.dungeon_mission_complete(mission_id=24093004)
            self.dungeon_mission_complete(mission_id=24093005)
            return 전투_종료(self.ctx)
        if self.dungeon_play_time() <= 70 and self.monster_dead(spawn_ids=[241,242,243,244,245,246,247,248]):
            # <중국용 컨디션체크>
            self.dungeon_mission_complete(mission_id=24093004)
            self.dungeon_mission_complete(mission_id=24093006)
            return 전투_종료(self.ctx)
        if self.dungeon_play_time() <= 270 and self.monster_dead(spawn_ids=[241,242,243,244,245,246,247,248]):
            # <NA용 컨디션체크>
            self.dungeon_mission_complete(mission_id=24093004)
            self.dungeon_mission_complete(mission_id=24093007)
            return 전투_종료(self.ctx)
        if self.monster_dead(spawn_ids=[241,242,243,244,245,246,247,248]):
            self.dungeon_mission_complete(mission_id=24093004)
            return 전투_종료(self.ctx)
        if not self.user_detected(box_ids=[901]):
            return 전투_종료(self.ctx)
        if self.dungeon_play_time() >= 300:
            return 전투_종료(self.ctx)


class 전투_종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_set_end_time()
        self.dungeon_close_timer()
        self.set_ai_extra_data(key='Autofire', value=0) # <대포 쏘기 중지 AI에 신호쏴주기>
        self.set_event_ui_round(rounds=[0,0])
        self.init_npc_rotation(spawn_ids=[102,103])
        self.destroy_monster(spawn_ids=[201])
        self.destroy_monster(spawn_ids=[211])
        self.destroy_monster(spawn_ids=[221,222,223,224,225,226,227])
        self.destroy_monster(spawn_ids=[231,232,233,234,235,236,237])
        # <네이린이랑 대포가 NPC이기 때문에 선택적으로 소멸시킴>
        self.destroy_monster(spawn_ids=[241,242,243,244,245,246,247,248])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 종료신호(self.ctx)


class 종료신호(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99990001, key='End', value=1)


initial_state = 대기
