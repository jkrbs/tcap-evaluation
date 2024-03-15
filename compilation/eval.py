import json

def eval_power_file(path):
    with open(path, 'r') as f:
        print(path)

        data = json.loads(f.read())
        clock_to_lat = 0
        clock = 0
        for stage in data['stage_characteristics']:
            clock_to_lat += stage["cycles_contribute_to_latency"]
            clock += stage["clock_cycles"]
        print(f"clock cycles: {clock}, added to latency: {clock_to_lat}")



if __name__ == '__main__':
    eval_power_file("power-cap-table-in-sram.json")
    eval_power_file("power-cap-table-in-tcam.json")
