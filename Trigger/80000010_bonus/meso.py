""" trigger/80000010_bonus/meso.xml """
import trigger_api


class 입장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[301]):
            return 완료(self.ctx)


class 완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_item(spawn_ids=[201])
        self.create_item(spawn_ids=[202])
        self.create_item(spawn_ids=[203])
        self.create_item(spawn_ids=[204])
        self.create_item(spawn_ids=[205])
        self.create_item(spawn_ids=[206])
        self.create_item(spawn_ids=[207])
        self.create_item(spawn_ids=[208])
        self.create_item(spawn_ids=[209])
        self.create_item(spawn_ids=[210])
        self.create_item(spawn_ids=[211])
        self.create_item(spawn_ids=[212])
        self.create_item(spawn_ids=[213])
        self.create_item(spawn_ids=[214])
        self.create_item(spawn_ids=[215])
        self.create_item(spawn_ids=[216])
        self.create_item(spawn_ids=[217])
        self.create_item(spawn_ids=[218])
        self.create_item(spawn_ids=[219])
        self.create_item(spawn_ids=[220])
        self.create_item(spawn_ids=[221])
        self.create_item(spawn_ids=[222])
        self.create_item(spawn_ids=[223])
        self.create_item(spawn_ids=[224])
        self.create_item(spawn_ids=[225])
        self.create_item(spawn_ids=[226])
        self.create_item(spawn_ids=[227])
        self.create_item(spawn_ids=[228])
        self.create_item(spawn_ids=[229])
        self.create_item(spawn_ids=[230])
        self.create_item(spawn_ids=[231])
        self.create_item(spawn_ids=[232])
        self.create_item(spawn_ids=[233])
        self.create_item(spawn_ids=[234])
        self.create_item(spawn_ids=[235])
        self.create_item(spawn_ids=[236])
        self.create_item(spawn_ids=[237])
        self.create_item(spawn_ids=[238])
        self.create_item(spawn_ids=[239])
        self.create_item(spawn_ids=[240])
        self.create_item(spawn_ids=[241])
        self.create_item(spawn_ids=[242])
        self.create_item(spawn_ids=[243])
        self.create_item(spawn_ids=[244])
        self.create_item(spawn_ids=[245])
        self.create_item(spawn_ids=[246])
        self.create_item(spawn_ids=[247])
        self.create_item(spawn_ids=[248])
        self.create_item(spawn_ids=[249])
        self.create_item(spawn_ids=[250])
        self.create_item(spawn_ids=[251])
        self.create_item(spawn_ids=[252])
        self.create_item(spawn_ids=[253])
        self.create_item(spawn_ids=[254])
        self.create_item(spawn_ids=[255])
        self.create_item(spawn_ids=[256])
        self.create_item(spawn_ids=[257])
        self.create_item(spawn_ids=[258])
        self.create_item(spawn_ids=[259])
        self.create_item(spawn_ids=[260])
        self.create_item(spawn_ids=[261])
        self.create_item(spawn_ids=[262])
        self.create_item(spawn_ids=[263])
        self.create_item(spawn_ids=[264])
        self.create_item(spawn_ids=[265])
        self.create_item(spawn_ids=[266])
        self.create_item(spawn_ids=[267])
        self.create_item(spawn_ids=[268])
        self.create_item(spawn_ids=[269])
        self.create_item(spawn_ids=[270])
        self.create_item(spawn_ids=[9001,9002,9003,9004,9005])
        self.set_timer(timer_id='1', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 완료2(self.ctx)


class 완료2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154])


initial_state = 입장
