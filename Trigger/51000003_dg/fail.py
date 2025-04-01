""" trigger/51000003_dg/fail.xml """
import trigger_api


class gameset(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Fail') == 1:
            return Fail_condition(self.ctx)


class Fail_condition(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=799) >= 1:
            return Fail(self.ctx)
        if self.count_users(box_id=705) >= 1:
            return Fail(self.ctx)
        if not self.user_detected(box_ids=[701]):
            return Fail(self.ctx)


class Fail(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Ending_Popup_01')
        self.set_timer(timer_id='10', seconds=10, display=True)
        self.select_camera_path(path_ids=[8800], return_view=False) # 카메라 뒤로 당김
        self.arcade_boom_boom_ocean_end_game()
        self.set_user_value(trigger_id=991104, key='Reset', value=1) # wave_projectile.xml
        self.set_user_value(trigger_id=991105, key='Reset', value=1) # wave_projectile_02.xml
        self.set_user_value(trigger_id=991106, key='Reset', value=1) # cannon_projectile.xml
        self.set_user_value(trigger_id=991107, key='Reset', value=1) # normal_projectile.xml
        self.set_user_value(trigger_id=991108, key='Reset', value=1) # fog.xml
        self.set_user_value(trigger_id=991111, key='Round_01', value=0) # item_01.xml
        self.set_user_value(trigger_id=991120, key='Reset', value=1) # wave_projectile_03.xml
        self.set_user_value(trigger_id=991121, key='Reset', value=1) # wave_projectile_04.xml
        self.set_user_value(trigger_id=991122, key='Reset', value=1) # wave_projectile_05.xml
        # normal_projectile_02.xml
        self.set_user_value(trigger_id=991123, key='Reset', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='10'):
            return End(self.ctx)


class End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(box_id=705)


initial_state = gameset
