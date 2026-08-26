#!/bin/bash
cd public/learning/챕터3_완성동영상/

# Function to tone down and extract poster
process_video() {
  local input="$1"
  local base="$2"
  
  if [ -f "$input" ]; then
    echo "Processing $input -> $base.mp4"
    # Apply Option D Tone Down (sat=0.45, gamma=1.15)
    ffmpeg -y -i "$input" -vf "eq=saturation=0.45:gamma=1.15" -c:v libx264 -crf 18 -preset fast -movflags +faststart -an "tmp_$base.mp4" </dev/null
    mv "tmp_$base.mp4" "$base.mp4"
    
    # Extract Poster from END frame
    ffmpeg -y -sseof -0.5 -i "$base.mp4" -frames:v 1 -q:v 2 "$base-poster.jpg" </dev/null
  fi
}

process_video "Ferris_wheel_animation_202608061947.mp4" "scene-ch3-01"
process_video "Rollercoaster_drawing_with_water…_202608061527.mp4" "scene-ch3-02"
process_video "Boy_and_girl_in_bumper_202608062001.mp4" "scene-ch3-03"

# Clean up old files
rm -f Ferris_wheel*.mp4 Rollercoaster*.mp4 Boy_and_girl*.mp4
