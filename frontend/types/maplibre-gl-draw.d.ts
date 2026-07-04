declare module "maplibre-gl-draw" {
  import type { IControl } from "maplibre-gl";

  type DrawControlOptions = {
    displayControlsDefault?: boolean;
    controls?: {
      polygon?: boolean;
      trash?: boolean;
      point?: boolean;
      line_string?: boolean;
      combine_features?: boolean;
      uncombine_features?: boolean;
    };
  };

  export default class MaplibreDraw implements IControl {
    constructor(options?: DrawControlOptions);
    getAll(): GeoJSON.FeatureCollection;
    onAdd(map: maplibregl.Map): HTMLElement;
    onRemove(map: maplibregl.Map): void;
  }
}
