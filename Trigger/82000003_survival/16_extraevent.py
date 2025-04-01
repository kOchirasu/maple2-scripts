""" trigger/82000003_survival/16_extraevent.xml """
import trigger_api


class Setting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[9000], skill_id=70001101, level=1, ignore_player=False, is_skill_set=False) # 변신 탈 것 해제용 버프
        self.set_gravity(gravity=0.0)
        self.remove_buff(box_id=9000, skill_id=71000075)
        self.remove_buff(box_id=9000, skill_id=71000052)
        self.remove_buff(box_id=9000, skill_id=71000076)
        self.set_user_value(key='ExtraEventCheck', value=0)
        self.set_user_value(key='ExtraEventOff', value=0)
        self.set_user_value(key='ExtraEventTestOn', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        # ExtraEventOn / ExtraEventRandomDelay01 / ExtraEvent01_Fast / ExtraEvent02_MapHack / ExtraEvent03_RobotSpawn / ExtraEvent04_DogEverywhere / ExtraEvent05_SkillCoolDownTimeReduce / ExtraEvent06_NoMoreFarming
        if self.user_value(key='ExtraEventTestOn') == 1:
            # test용 수정 가능 지점 : 발동 시킬 이벤트 종류
            return ExtraEventOn(self.ctx)
        if self.user_value(key='ExtraEventCheck') == 1:
            # ExtraEventOccurrenceProbability / ExtraEventOn
            return ExtraEventOccurrenceProbability(self.ctx)


class ExtraEventOccurrenceProbability(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=60.0):
            return ExtraEventOff(self.ctx)
        if self.random_condition(weight=40.0):
            return ExtraEventOn(self.ctx)
        if self.user_value(key='ExtraEventOff') == 1:
            return Quit(self.ctx)


class ExtraEventOff(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ExtraEventOff') == 1:
            return Quit(self.ctx)


class ExtraEventOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.write_log(log_name='Survival', event='MokumEventOn') # 모쿰 이벤트 로그 - 모쿰 소환 됨

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return RelicLeft05(self.ctx)


class RelicLeft05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=11, key='RelicMobSpawn', value=1)
        self.set_user_value(trigger_id=12, key='RelicMobSpawn', value=1)
        self.set_user_value(trigger_id=13, key='RelicMobSpawn', value=1)
        self.set_user_value(trigger_id=14, key='RelicMobSpawn', value=1)
        self.set_user_value(trigger_id=15, key='RelicMobSpawn', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RelicMobRedDie') == 1:
            return RelicLeft04_NoRed(self.ctx)
        if self.user_value(key='RelicMobSkyblueDie') == 1:
            return RelicLeft04_NoSkyblue(self.ctx)
        if self.user_value(key='RelicMobGreenDie') == 1:
            return RelicLeft04_NoGreen(self.ctx)
        if self.user_value(key='RelicMobYellowDie') == 1:
            return RelicLeft04_NoYellow(self.ctx)
        if self.user_value(key='RelicMobGreyDie') == 1:
            return RelicLeft04_NoGrey(self.ctx)
        if self.user_value(key='ExtraEventOff') == 1:
            return Quit(self.ctx)

    def on_exit(self) -> None:
        self.play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        self.play_system_sound_in_box(sound='System_Mokum_Die_01')
        # 가이드 : [b:첫 번째] 모쿰이 잡혔습니다!
        self.show_guide_summary(entity_id=28200002, text_id=28200002, duration=4000)
        self.side_npc_talk_bottom(npc_id=21001019, illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__0$')


# 4 마리 남음
class RelicLeft04_NoRed(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.write_log(log_name='Survival', event='MokumKill_01') # 모쿰 이벤트 로그 - 4마리 남음

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RelicMobSkyblueDie') == 1:
            return RelicLeft03_NoRed_NoSkyblue(self.ctx)
        if self.user_value(key='RelicMobGreenDie') == 1:
            return RelicLeft03_NoRed_NoGreen(self.ctx)
        if self.user_value(key='RelicMobYellowDie') == 1:
            return RelicLeft03_NoRed_NoYellow(self.ctx)
        if self.user_value(key='RelicMobGreyDie') == 1:
            return RelicLeft03_NoRed_NoGrey(self.ctx)
        if self.user_value(key='ExtraEventOff') == 1:
            return Quit(self.ctx)

    def on_exit(self) -> None:
        self.play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        self.play_system_sound_in_box(sound='System_Mokum_Die_01')
        # 가이드 : [b:두 번째] 모쿰이 잡혔습니다!
        self.show_guide_summary(entity_id=28200003, text_id=28200003, duration=3000)
        self.side_npc_talk_bottom(npc_id=21001019, illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__1$')


class RelicLeft04_NoSkyblue(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RelicMobRedDie') == 1:
            return RelicLeft03_NoRed_NoSkyblue(self.ctx)
        if self.user_value(key='RelicMobGreenDie') == 1:
            return RelicLeft03_NoSkyblue_NoGreen(self.ctx)
        if self.user_value(key='RelicMobYellowDie') == 1:
            return RelicLeft03_NoSkyblue_NoYellow(self.ctx)
        if self.user_value(key='RelicMobGreyDie') == 1:
            return RelicLeft03_NoSkyblue_NoGrey(self.ctx)
        if self.user_value(key='ExtraEventOff') == 1:
            return Quit(self.ctx)

    def on_exit(self) -> None:
        self.play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        self.play_system_sound_in_box(sound='System_Mokum_Die_01')
        # 가이드 : [b:두 번째] 모쿰이 잡혔습니다!
        self.show_guide_summary(entity_id=28200003, text_id=28200003, duration=3000)
        self.side_npc_talk_bottom(npc_id=21001019, illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__1$')


class RelicLeft04_NoGreen(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RelicMobRedDie') == 1:
            return RelicLeft03_NoRed_NoGreen(self.ctx)
        if self.user_value(key='RelicMobSkyblueDie') == 1:
            return RelicLeft03_NoSkyblue_NoGreen(self.ctx)
        if self.user_value(key='RelicMobYellowDie') == 1:
            return RelicLeft03_NoGreen_NoYellow(self.ctx)
        if self.user_value(key='RelicMobGreyDie') == 1:
            return RelicLeft03_NoGreen_NoGrey(self.ctx)
        if self.user_value(key='ExtraEventOff') == 1:
            return Quit(self.ctx)

    def on_exit(self) -> None:
        self.play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        self.play_system_sound_in_box(sound='System_Mokum_Die_01')
        # 가이드 : [b:두 번째] 모쿰이 잡혔습니다!
        self.show_guide_summary(entity_id=28200003, text_id=28200003, duration=3000)
        self.side_npc_talk_bottom(npc_id=21001019, illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__1$')


class RelicLeft04_NoYellow(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RelicMobRedDie') == 1:
            return RelicLeft03_NoRed_NoYellow(self.ctx)
        if self.user_value(key='RelicMobSkyblueDie') == 1:
            return RelicLeft03_NoSkyblue_NoYellow(self.ctx)
        if self.user_value(key='RelicMobGreenDie') == 1:
            return RelicLeft03_NoGreen_NoYellow(self.ctx)
        if self.user_value(key='RelicMobGreyDie') == 1:
            return RelicLeft03_NoYellow_NoGrey(self.ctx)
        if self.user_value(key='ExtraEventOff') == 1:
            return Quit(self.ctx)

    def on_exit(self) -> None:
        self.play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        self.play_system_sound_in_box(sound='System_Mokum_Die_01')
        # 가이드 : [b:두 번째] 모쿰이 잡혔습니다!
        self.show_guide_summary(entity_id=28200003, text_id=28200003, duration=3000)
        self.side_npc_talk_bottom(npc_id=21001019, illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__1$')


class RelicLeft04_NoGrey(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RelicMobRedDie') == 1:
            return RelicLeft03_NoRed_NoGrey(self.ctx)
        if self.user_value(key='RelicMobSkyblueDie') == 1:
            return RelicLeft03_NoSkyblue_NoGrey(self.ctx)
        if self.user_value(key='RelicMobGreenDie') == 1:
            return RelicLeft03_NoGreen_NoGrey(self.ctx)
        if self.user_value(key='RelicMobYellowDie') == 1:
            return RelicLeft03_NoYellow_NoGrey(self.ctx)
        if self.user_value(key='ExtraEventOff') == 1:
            return Quit(self.ctx)

    def on_exit(self) -> None:
        self.play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        self.play_system_sound_in_box(sound='System_Mokum_Die_01')
        # 가이드 : [b:두 번째] 모쿰이 잡혔습니다!
        self.show_guide_summary(entity_id=28200003, text_id=28200003, duration=3000)
        self.side_npc_talk_bottom(npc_id=21001019, illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__1$')


# 3 마리 남음
class RelicLeft03_NoRed_NoSkyblue(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.write_log(log_name='Survival', event='MokumKill_02') # 모쿰 이벤트 로그 - 3마리 남음

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RelicMobGreenDie') == 1:
            return RelicLeft02_NoRed_NoSkyblue_NoGreen(self.ctx)
        if self.user_value(key='RelicMobYellowDie') == 1:
            return RelicLeft02_NoRed_NoSkyblue_NoYellow(self.ctx)
        if self.user_value(key='RelicMobGreyDie') == 1:
            return RelicLeft02_NoRed_NoSkyblue_NoGrey(self.ctx)
        if self.user_value(key='ExtraEventOff') == 1:
            return Quit(self.ctx)

    def on_exit(self) -> None:
        self.play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        self.play_system_sound_in_box(sound='System_Mokum_Die_01')
        # 가이드 : [b:세 번째] 모쿰이 잡혔습니다!
        self.show_guide_summary(entity_id=28200004, text_id=28200004, duration=3000)
        self.side_npc_talk_bottom(npc_id=21001019, illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__2$')


class RelicLeft03_NoRed_NoGreen(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RelicMobSkyblueDie') == 1:
            return RelicLeft02_NoRed_NoSkyblue_NoGreen(self.ctx)
        if self.user_value(key='RelicMobYellowDie') == 1:
            return RelicLeft02_NoRed_NoGreen_NoYellow(self.ctx)
        if self.user_value(key='RelicMobGreyDie') == 1:
            return RelicLeft02_NoRed_NoGreen_NoGrey(self.ctx)
        if self.user_value(key='ExtraEventOff') == 1:
            return Quit(self.ctx)

    def on_exit(self) -> None:
        self.play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        self.play_system_sound_in_box(sound='System_Mokum_Die_01')
        # 가이드 : [b:세 번째] 모쿰이 잡혔습니다!
        self.show_guide_summary(entity_id=28200004, text_id=28200004, duration=3000)
        self.side_npc_talk_bottom(npc_id=21001019, illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__2$')


class RelicLeft03_NoRed_NoYellow(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RelicMobSkyblueDie') == 1:
            return RelicLeft02_NoRed_NoSkyblue_NoYellow(self.ctx)
        if self.user_value(key='RelicMobGreenDie') == 1:
            return RelicLeft02_NoRed_NoGreen_NoYellow(self.ctx)
        if self.user_value(key='RelicMobGreyDie') == 1:
            return RelicLeft02_NoRed_NoYellow_NoGrey(self.ctx)
        if self.user_value(key='ExtraEventOff') == 1:
            return Quit(self.ctx)

    def on_exit(self) -> None:
        self.play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        self.play_system_sound_in_box(sound='System_Mokum_Die_01')
        # 가이드 : [b:세 번째] 모쿰이 잡혔습니다!
        self.show_guide_summary(entity_id=28200004, text_id=28200004, duration=3000)
        self.side_npc_talk_bottom(npc_id=21001019, illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__2$')


class RelicLeft03_NoRed_NoGrey(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RelicMobSkyblueDie') == 1:
            return RelicLeft02_NoRed_NoSkyblue_NoGrey(self.ctx)
        if self.user_value(key='RelicMobGreenDie') == 1:
            return RelicLeft02_NoRed_NoGreen_NoGrey(self.ctx)
        if self.user_value(key='RelicMobYellowDie') == 1:
            return RelicLeft02_NoRed_NoYellow_NoGrey(self.ctx)
        if self.user_value(key='ExtraEventOff') == 1:
            return Quit(self.ctx)

    def on_exit(self) -> None:
        self.play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        self.play_system_sound_in_box(sound='System_Mokum_Die_01')
        # 가이드 : [b:세 번째] 모쿰이 잡혔습니다!
        self.show_guide_summary(entity_id=28200004, text_id=28200004, duration=3000)
        self.side_npc_talk_bottom(npc_id=21001019, illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__2$')


class RelicLeft03_NoSkyblue_NoGreen(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RelicMobRedDie') == 1:
            return RelicLeft02_NoRed_NoSkyblue_NoGreen(self.ctx)
        if self.user_value(key='RelicMobYellowDie') == 1:
            return RelicLeft02_NoSkyblue_NoGreen_NoYellow(self.ctx)
        if self.user_value(key='RelicMobGreyDie') == 1:
            return RelicLeft02_NoSkyblue_NoGreen_NoGrey(self.ctx)
        if self.user_value(key='ExtraEventOff') == 1:
            return Quit(self.ctx)

    def on_exit(self) -> None:
        self.play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        self.play_system_sound_in_box(sound='System_Mokum_Die_01')
        # 가이드 : [b:세 번째] 모쿰이 잡혔습니다!
        self.show_guide_summary(entity_id=28200004, text_id=28200004, duration=3000)
        self.side_npc_talk_bottom(npc_id=21001019, illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__2$')


class RelicLeft03_NoSkyblue_NoYellow(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RelicMobRedDie') == 1:
            return RelicLeft02_NoRed_NoSkyblue_NoYellow(self.ctx)
        if self.user_value(key='RelicMobGreenDie') == 1:
            return RelicLeft02_NoSkyblue_NoGreen_NoYellow(self.ctx)
        if self.user_value(key='RelicMobGreyDie') == 1:
            return RelicLeft02_NoSkyblue_NoYellow_NoGrey(self.ctx)
        if self.user_value(key='ExtraEventOff') == 1:
            return Quit(self.ctx)

    def on_exit(self) -> None:
        self.play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        self.play_system_sound_in_box(sound='System_Mokum_Die_01')
        # 가이드 : [b:세 번째] 모쿰이 잡혔습니다!
        self.show_guide_summary(entity_id=28200004, text_id=28200004, duration=3000)
        self.side_npc_talk_bottom(npc_id=21001019, illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__2$')


class RelicLeft03_NoSkyblue_NoGrey(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RelicMobRedDie') == 1:
            return RelicLeft02_NoRed_NoSkyblue_NoGrey(self.ctx)
        if self.user_value(key='RelicMobGreenDie') == 1:
            return RelicLeft02_NoSkyblue_NoGreen_NoGrey(self.ctx)
        if self.user_value(key='RelicMobYellowDie') == 1:
            return RelicLeft02_NoSkyblue_NoYellow_NoGrey(self.ctx)
        if self.user_value(key='ExtraEventOff') == 1:
            return Quit(self.ctx)

    def on_exit(self) -> None:
        self.play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        self.play_system_sound_in_box(sound='System_Mokum_Die_01')
        # 가이드 : [b:세 번째] 모쿰이 잡혔습니다!
        self.show_guide_summary(entity_id=28200004, text_id=28200004, duration=3000)
        self.side_npc_talk_bottom(npc_id=21001019, illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__2$')


class RelicLeft03_NoGreen_NoYellow(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RelicMobRedDie') == 1:
            return RelicLeft02_NoRed_NoGreen_NoYellow(self.ctx)
        if self.user_value(key='RelicMobSkyblueDie') == 1:
            return RelicLeft02_NoSkyblue_NoGreen_NoYellow(self.ctx)
        if self.user_value(key='RelicMobGreyDie') == 1:
            return RelicLeft02_NoGreen_NoYellow_NoGrey(self.ctx)
        if self.user_value(key='ExtraEventOff') == 1:
            return Quit(self.ctx)

    def on_exit(self) -> None:
        self.play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        self.play_system_sound_in_box(sound='System_Mokum_Die_01')
        # 가이드 : [b:세 번째] 모쿰이 잡혔습니다!
        self.show_guide_summary(entity_id=28200004, text_id=28200004, duration=3000)
        self.side_npc_talk_bottom(npc_id=21001019, illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__2$')


class RelicLeft03_NoGreen_NoGrey(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RelicMobRedDie') == 1:
            return RelicLeft02_NoRed_NoGreen_NoGrey(self.ctx)
        if self.user_value(key='RelicMobSkyblueDie') == 1:
            return RelicLeft02_NoSkyblue_NoGreen_NoGrey(self.ctx)
        if self.user_value(key='RelicMobYellowDie') == 1:
            return RelicLeft02_NoGreen_NoYellow_NoGrey(self.ctx)
        if self.user_value(key='ExtraEventOff') == 1:
            return Quit(self.ctx)

    def on_exit(self) -> None:
        self.play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        self.play_system_sound_in_box(sound='System_Mokum_Die_01')
        # 가이드 : [b:세 번째] 모쿰이 잡혔습니다!
        self.show_guide_summary(entity_id=28200004, text_id=28200004, duration=3000)
        self.side_npc_talk_bottom(npc_id=21001019, illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__2$')


class RelicLeft03_NoYellow_NoGrey(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RelicMobRedDie') == 1:
            return RelicLeft02_NoRed_NoYellow_NoGrey(self.ctx)
        if self.user_value(key='RelicMobSkyblueDie') == 1:
            return RelicLeft02_NoSkyblue_NoYellow_NoGrey(self.ctx)
        if self.user_value(key='RelicMobGreenDie') == 1:
            return RelicLeft02_NoGreen_NoYellow_NoGrey(self.ctx)
        if self.user_value(key='ExtraEventOff') == 1:
            return Quit(self.ctx)

    def on_exit(self) -> None:
        self.play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        self.play_system_sound_in_box(sound='System_Mokum_Die_01')
        # 가이드 : [b:세 번째] 모쿰이 잡혔습니다!
        self.show_guide_summary(entity_id=28200004, text_id=28200004, duration=3000)
        self.side_npc_talk_bottom(npc_id=21001019, illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__2$')


# 2 마리 남음
class RelicLeft02_NoRed_NoSkyblue_NoGreen(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.write_log(log_name='Survival', event='MokumKill_03') # 모쿰 이벤트 로그 - 2마리 남음

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RelicMobYellowDie') == 1:
            return RelicLeft01_OnlyGrey(self.ctx)
        if self.user_value(key='RelicMobGreyDie') == 1:
            return RelicLeft01_OnlyYellow(self.ctx)
        if self.user_value(key='ExtraEventOff') == 1:
            return Quit(self.ctx)

    def on_exit(self) -> None:
        self.play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        self.play_system_sound_in_box(sound='System_Mokum_Die_01')
        # 가이드 : [b:네 번째] 모쿰이 잡혔습니다!
        self.show_guide_summary(entity_id=28200005, text_id=28200005, duration=3000)
        self.side_npc_talk_bottom(npc_id=21001019, illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__3$')


class RelicLeft02_NoRed_NoSkyblue_NoYellow(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RelicMobGreenDie') == 1:
            return RelicLeft01_OnlyGrey(self.ctx)
        if self.user_value(key='RelicMobGreyDie') == 1:
            return RelicLeft01_OnlyGreen(self.ctx)
        if self.user_value(key='ExtraEventOff') == 1:
            return Quit(self.ctx)

    def on_exit(self) -> None:
        self.play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        self.play_system_sound_in_box(sound='System_Mokum_Die_01')
        # 가이드 : [b:네 번째] 모쿰이 잡혔습니다!
        self.show_guide_summary(entity_id=28200005, text_id=28200005, duration=3000)
        self.side_npc_talk_bottom(npc_id=21001019, illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__3$')


class RelicLeft02_NoRed_NoSkyblue_NoGrey(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RelicMobGreenDie') == 1:
            return RelicLeft01_OnlyYellow(self.ctx)
        if self.user_value(key='RelicMobYellowDie') == 1:
            return RelicLeft01_OnlyGreen(self.ctx)
        if self.user_value(key='ExtraEventOff') == 1:
            return Quit(self.ctx)

    def on_exit(self) -> None:
        self.play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        self.play_system_sound_in_box(sound='System_Mokum_Die_01')
        # 가이드 : [b:네 번째] 모쿰이 잡혔습니다!
        self.show_guide_summary(entity_id=28200005, text_id=28200005, duration=3000)
        self.side_npc_talk_bottom(npc_id=21001019, illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__3$')


class RelicLeft02_NoRed_NoGreen_NoYellow(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RelicMobSkyblueDie') == 1:
            return RelicLeft01_OnlyGrey(self.ctx)
        if self.user_value(key='RelicMobGreyDie') == 1:
            return RelicLeft01_OnlySkyblue(self.ctx)
        if self.user_value(key='ExtraEventOff') == 1:
            return Quit(self.ctx)

    def on_exit(self) -> None:
        self.play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        self.play_system_sound_in_box(sound='System_Mokum_Die_01')
        # 가이드 : [b:네 번째] 모쿰이 잡혔습니다!
        self.show_guide_summary(entity_id=28200005, text_id=28200005, duration=3000)
        self.side_npc_talk_bottom(npc_id=21001019, illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__3$')


class RelicLeft02_NoRed_NoGreen_NoGrey(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RelicMobSkyblueDie') == 1:
            return RelicLeft01_OnlyYellow(self.ctx)
        if self.user_value(key='RelicMobYellowDie') == 1:
            return RelicLeft01_OnlySkyblue(self.ctx)
        if self.user_value(key='ExtraEventOff') == 1:
            return Quit(self.ctx)

    def on_exit(self) -> None:
        self.play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        self.play_system_sound_in_box(sound='System_Mokum_Die_01')
        # 가이드 : [b:네 번째] 모쿰이 잡혔습니다!
        self.show_guide_summary(entity_id=28200005, text_id=28200005, duration=3000)
        self.side_npc_talk_bottom(npc_id=21001019, illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__3$')


class RelicLeft02_NoRed_NoYellow_NoGrey(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RelicMobSkyblueDie') == 1:
            return RelicLeft01_OnlyGreen(self.ctx)
        if self.user_value(key='RelicMobGreenDie') == 1:
            return RelicLeft01_OnlySkyblue(self.ctx)
        if self.user_value(key='ExtraEventOff') == 1:
            return Quit(self.ctx)

    def on_exit(self) -> None:
        self.play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        self.play_system_sound_in_box(sound='System_Mokum_Die_01')
        # 가이드 : [b:네 번째] 모쿰이 잡혔습니다!
        self.show_guide_summary(entity_id=28200005, text_id=28200005, duration=3000)
        self.side_npc_talk_bottom(npc_id=21001019, illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__3$')


class RelicLeft02_NoSkyblue_NoGreen_NoYellow(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RelicMobRedDie') == 1:
            return RelicLeft01_OnlyGrey(self.ctx)
        if self.user_value(key='RelicMobGreyDie') == 1:
            return RelicLeft01_OnlyRed(self.ctx)
        if self.user_value(key='ExtraEventOff') == 1:
            return Quit(self.ctx)

    def on_exit(self) -> None:
        self.play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        self.play_system_sound_in_box(sound='System_Mokum_Die_01')
        # 가이드 : [b:네 번째] 모쿰이 잡혔습니다!
        self.show_guide_summary(entity_id=28200005, text_id=28200005, duration=3000)
        self.side_npc_talk_bottom(npc_id=21001019, illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__3$')


class RelicLeft02_NoSkyblue_NoGreen_NoGrey(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RelicMobRedDie') == 1:
            return RelicLeft01_OnlyYellow(self.ctx)
        if self.user_value(key='RelicMobYellowDie') == 1:
            return RelicLeft01_OnlyRed(self.ctx)
        if self.user_value(key='ExtraEventOff') == 1:
            return Quit(self.ctx)

    def on_exit(self) -> None:
        self.play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        self.play_system_sound_in_box(sound='System_Mokum_Die_01')
        # 가이드 : [b:네 번째] 모쿰이 잡혔습니다!
        self.show_guide_summary(entity_id=28200005, text_id=28200005, duration=3000)
        self.side_npc_talk_bottom(npc_id=21001019, illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__3$')


class RelicLeft02_NoSkyblue_NoYellow_NoGrey(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RelicMobRedDie') == 1:
            return RelicLeft01_OnlyGreen(self.ctx)
        if self.user_value(key='RelicMobGreenDie') == 1:
            return RelicLeft01_OnlyRed(self.ctx)
        if self.user_value(key='ExtraEventOff') == 1:
            return Quit(self.ctx)

    def on_exit(self) -> None:
        self.play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        self.play_system_sound_in_box(sound='System_Mokum_Die_01')
        # 가이드 : [b:네 번째] 모쿰이 잡혔습니다!
        self.show_guide_summary(entity_id=28200005, text_id=28200005, duration=3000)
        self.side_npc_talk_bottom(npc_id=21001019, illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__3$')


class RelicLeft02_NoGreen_NoYellow_NoGrey(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RelicMobRedDie') == 1:
            return RelicLeft01_OnlySkyblue(self.ctx)
        if self.user_value(key='RelicMobSkyblueDie') == 1:
            return RelicLeft01_OnlyRed(self.ctx)
        if self.user_value(key='ExtraEventOff') == 1:
            return Quit(self.ctx)

    def on_exit(self) -> None:
        self.play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        self.play_system_sound_in_box(sound='System_Mokum_Die_01')
        # 가이드 : [b:네 번째] 모쿰이 잡혔습니다!
        self.show_guide_summary(entity_id=28200005, text_id=28200005, duration=3000)
        self.side_npc_talk_bottom(npc_id=21001019, illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__3$')


# 1 마리 남음
class RelicLeft01_OnlyRed(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.write_log(log_name='Survival', event='MokumKill_04') # 모쿰 이벤트 로그 - 1마리 남음

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RelicMobRedDie') == 1:
            return ExtraEventRandomDelay01(self.ctx)
        if self.user_value(key='ExtraEventOff') == 1:
            return Quit(self.ctx)

    def on_exit(self) -> None:
        self.play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        self.play_system_sound_in_box(sound='System_Mokum_Die_01')
        # 가이드 : [b:마지막] 모쿰이 잡혔습니다!
        self.show_guide_summary(entity_id=28200006, text_id=28200006, duration=3000)
        self.side_npc_talk_bottom(npc_id=21001019, illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__4$')


class RelicLeft01_OnlySkyblue(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RelicMobSkyblueDie') == 1:
            return ExtraEventRandomDelay01(self.ctx)
        if self.user_value(key='ExtraEventOff') == 1:
            return Quit(self.ctx)

    def on_exit(self) -> None:
        self.play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        self.play_system_sound_in_box(sound='System_Mokum_Die_01')
        # 가이드 : [b:마지막] 모쿰이 잡혔습니다!
        self.show_guide_summary(entity_id=28200006, text_id=28200006, duration=3000)
        self.side_npc_talk_bottom(npc_id=21001019, illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__4$')


class RelicLeft01_OnlyGreen(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RelicMobGreenDie') == 1:
            return ExtraEventRandomDelay01(self.ctx)
        if self.user_value(key='ExtraEventOff') == 1:
            return Quit(self.ctx)

    def on_exit(self) -> None:
        self.play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        self.play_system_sound_in_box(sound='System_Mokum_Die_01')
        # 가이드 : [b:마지막] 모쿰이 잡혔습니다!
        self.show_guide_summary(entity_id=28200006, text_id=28200006, duration=3000)
        self.side_npc_talk_bottom(npc_id=21001019, illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__4$')


class RelicLeft01_OnlyYellow(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RelicMobYellowDie') == 1:
            return ExtraEventRandomDelay01(self.ctx)
        if self.user_value(key='ExtraEventOff') == 1:
            return Quit(self.ctx)

    def on_exit(self) -> None:
        self.play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        self.play_system_sound_in_box(sound='System_Mokum_Die_01')
        # 가이드 : [b:마지막] 모쿰이 잡혔습니다!
        self.show_guide_summary(entity_id=28200006, text_id=28200006, duration=3000)
        self.side_npc_talk_bottom(npc_id=21001019, illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__4$')


class RelicLeft01_OnlyGrey(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RelicMobGreyDie') == 1:
            return ExtraEventRandomDelay01(self.ctx)
        if self.user_value(key='ExtraEventOff') == 1:
            return Quit(self.ctx)

    def on_exit(self) -> None:
        self.play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        self.play_system_sound_in_box(sound='System_Mokum_Die_01')
        # 가이드 : [b:마지막] 모쿰이 잡혔습니다!
        self.show_guide_summary(entity_id=28200006, text_id=28200006, duration=3000)
        self.side_npc_talk_bottom(npc_id=21001019, illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__4$')


class ExtraEventRandomDelay01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return ExtraEventRandomDelay02(self.ctx)
        if self.user_value(key='ExtraEventOff') == 1:
            return Quit(self.ctx)


class ExtraEventRandomDelay02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Mokum_Message_01')
        self.side_npc_talk_bottom(npc_id=21001019, illust='MushroomRichPorter_normal', duration=8000, script='$82000002_survival__16_ExtraEvent__5$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return ExtraEventRandomDelay03(self.ctx)
        if self.user_value(key='ExtraEventOff') == 1:
            return Quit(self.ctx)


class ExtraEventRandomDelay03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        self.show_guide_summary(entity_id=28200007, text_id=28200007, duration=4000) # 가이드 : 모쿰의 장난이 시작됩니다!
        self.write_log(log_name='Survival', event='MokumEventStart') # 모쿰 이벤트 로그 - 이벤트 시작

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return ExtraEventRandom(self.ctx) # ExtraEventRandom
        if self.user_value(key='ExtraEventOff') == 1:
            return Quit(self.ctx)


class ExtraEventRandom(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=20.0):
            return ExtraEvent01_Fast(self.ctx)
        if self.random_condition(weight=20.0):
            return ExtraEvent02_MapHack(self.ctx)
        if self.random_condition(weight=20.0):
            return ExtraEvent03_RobotSpawn(self.ctx)
        if self.random_condition(weight=20.0):
            return ExtraEvent04_SkillCoolDownTimeReduce(self.ctx)
        if self.random_condition(weight=20.0):
            return ExtraEvent05_NoMoreFarming(self.ctx)
        if self.user_value(key='ExtraEventOff') == 1:
            return Quit(self.ctx)


class ExtraEvent01_Fast(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.write_log(log_name='Survival', event='MokumEvent_01') # 모쿰 이벤트 로그 1
        self.play_system_sound_in_box(sound='System_Mokum_Completion_01')
        self.side_npc_talk_bottom(npc_id=21001019, illust='MushroomRichPorter_normal', duration=8000, script='$82000002_survival__16_ExtraEvent__6$')
        self.add_buff(box_ids=[9000], skill_id=71000075, level=1, ignore_player=False, is_skill_set=False)
        self.set_gravity(gravity=30.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ExtraEventOff') == 1:
            return Quit(self.ctx)


class ExtraEvent02_MapHack(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.write_log(log_name='Survival', event='MokumEvent_02') # 모쿰 이벤트 로그 2
        self.remove_buff(box_id=9000, skill_id=71000052)
        self.play_system_sound_in_box(sound='System_Mokum_Completion_01')
        self.side_npc_talk_bottom(npc_id=21001019, illust='MushroomRichPorter_normal', duration=8000, script='$82000002_survival__16_ExtraEvent__7$')
        self.add_buff(box_ids=[9000], skill_id=71000052, level=2, ignore_player=False, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ExtraEventOff') == 1:
            return Quit(self.ctx)


class ExtraEvent03_RobotSpawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.write_log(log_name='Survival', event='MokumEvent_03') # 모쿰 이벤트 로그 3
        self.play_system_sound_in_box(sound='System_Mokum_Completion_01')
        self.side_npc_talk_bottom(npc_id=21001019, illust='MushroomRichPorter_normal', duration=8000, script='$82000002_survival__16_ExtraEvent__8$')
        self.set_user_value(trigger_id=10, key='BattleRidingOnCount', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ExtraEventOff') == 1:
            return Quit(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(trigger_id=10, key='BattleRidingOff', value=1)


class ExtraEvent04_SkillCoolDownTimeReduce(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.write_log(log_name='Survival', event='MokumEvent_04') # 모쿰 이벤트 로그 4
        self.play_system_sound_in_box(sound='System_Mokum_Completion_01')
        self.side_npc_talk_bottom(npc_id=21001019, illust='MushroomRichPorter_normal', duration=8000, script='$82000002_survival__16_ExtraEvent__9$')
        self.add_buff(box_ids=[9000], skill_id=71000076, level=1, ignore_player=False, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ExtraEventOff') == 1:
            return Quit(self.ctx)


class ExtraEvent05_NoMoreFarming(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.write_log(log_name='Survival', event='MokumEvent_05') # 모쿰 이벤트 로그 5
        self.play_system_sound_in_box(sound='System_Mokum_Completion_01')
        self.side_npc_talk_bottom(npc_id=21001019, illust='MushroomRichPorter_normal', duration=8000, script='$82000002_survival__16_ExtraEvent__10$')
        self.start_combine_spawn(group_id=[355,356,357,358,359,360,361,362,363,364,365,366,367,368,369,370,371,372,373,374,375,376,377,378,379,380,381,382,383,384,385,386,387,388,389,390,391,392,393,394,395,396,397,398,399,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,420,421,422,423,424,425,426,427,428,429,430,431,432,433,434,435,436,437,438,439,440,441,442,443,444,445,446,447,448,449,450,451,452,453,454,455,456,457,458,459,460,461,462,463,464,465,466,467,468,469,470,471,472,473,474,475,476,477]) # 나태 버섯 Normal Mob
        # groupId="10000342-10000381" 황금 상자 Rare Box
        self.start_combine_spawn(group_id=[10000342,10000343,10000344,10000345,10000346,10000347,10000348,10000349,10000350,10000351,10000352,10000353,10000354,10000355,10000356,10000357,10000358,10000359,10000360,10000361,10000362,10000363,10000364,10000365,10000366,10000367,10000368,10000369,10000370,10000371,10000372,10000373,10000374,10000375,10000376,10000377,10000378,10000379,10000380,10000381])
        self.start_combine_spawn(group_id=[319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354]) # 축복의 슬라임 Rare Mob
        # 10000040-10000506 나무 상자 Normal Box
        self.start_combine_spawn(group_id=[10000382,10000383,10000384,10000385,10000386,10000387,10000388,10000389,10000390,10000391,10000392,10000393,10000394,10000395,10000396,10000397,10000398,10000399,10000400,10000401,10000402,10000403,10000404,10000405,10000406,10000407,10000408,10000409,10000410,10000411,10000412,10000413,10000414,10000415,10000416,10000417,10000418,10000419,10000420,10000421,10000422,10000423,10000424,10000425,10000426,10000427,10000428,10000429,10000430,10000431,10000432,10000433,10000434,10000435,10000436,10000437,10000438,10000439,10000440,10000441,10000442,10000443,10000444,10000445,10000446,10000447,10000448,10000449,10000450,10000451,10000452,10000453,10000454,10000455,10000456,10000457,10000458,10000459,10000460,10000461,10000462,10000463,10000464,10000465,10000466,10000467,10000468,10000469,10000470,10000471,10000472,10000473,10000474,10000475,10000476,10000477,10000478,10000479,10000480,10000481,10000482,10000483,10000484,10000485,10000486,10000487,10000488,10000489,10000490,10000491,10000492,10000493,10000494,10000495,10000496,10000497,10000498,10000499,10000500,10000501,10000502,10000503,10000504,10000505,10000506])
        self.set_user_value(trigger_id=5, key='RareBoxOff', value=1)
        self.set_user_value(trigger_id=8, key='RareMobOff', value=1)
        self.set_user_value(trigger_id=9, key='NormaBoxOff', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ExtraEventOff') == 1:
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=11, key='RelicMobRemove', value=1)
        self.set_user_value(trigger_id=12, key='RelicMobRemove', value=1)
        self.set_user_value(trigger_id=13, key='RelicMobRemove', value=1)
        self.set_user_value(trigger_id=14, key='RelicMobRemove', value=1)
        self.set_user_value(trigger_id=15, key='RelicMobRemove', value=1)


initial_state = Setting
