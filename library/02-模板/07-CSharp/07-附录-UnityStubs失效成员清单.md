# 附录：UnityStubs 1.7 失效成员完整清单

> 本附录是 `06-UnityStubs兼容层与失效API.md` 的配套数据。核对对象：`E:\SteamLibrary\steamapps\common\RimWorld\UnityStubs.dll`（**934** 个类型 / **6,653** 个方法，口径 Public + NonPublic + Instance + Static + DeclaredOnly）。
>
> 判定方式：用 IL 扫描找出每个方法体里对 `UnityStubs.Internal.StubWarner::LogStub`（MetadataToken 100663905）的**调用点** —— 有调用点即该方法是 stub，行为是「记一条警告 + 返回默认值 / 空操作」，**不抛异常**。
>
> 统计口径：**254 个调用点 / 230 个「类型 :: 成员」组合 / 覆盖 88 个类型**。同一成员被多处调用会重复计数，所以调用点数 ≥ 唯一成员数；更早一版报告按「方法体数量」统计为 257，差异来自重载与重复调用点的计数方式，**三者不矛盾**。

## 按类型汇总

| 类型 | stub 调用点 | 该类型 stub 成员 |
|---|---|---|
| `UnityEngine.Rendering.CommandBuffer` | 30 | `EnableScissorRect`、`DisableScissorRect`、`Clear`、`ClearRenderTarget`、`DispatchCompute`、`DrawMesh`、`SetViewProjectionMatrices`、`SetViewport`、`Blit`、`GetTemporaryRT`、`ReleaseTemporaryRT`、`SetGlobalTexture`、`SetRenderTarget`、`IssuePluginEvent`、`IssuePluginEventAndData`、`IssuePluginEventAndDataWithFlags`、`SetBufferData`、`SetComputeIntParam`、`SetExecutionFlags` |
| `UnityEngine.InputSystem.InputActionAsset` | 13 | `Contains`、`Disable`、`Enable`、`FindAction`、`get_bindingMask`、`set_bindingMask`、`get_bindings`、`get_controlSchemes`、`get_devices`、`set_devices`、`GetEnumerator`、`FindActionMap`、`System.Collections.IEnumerable.GetEnumerator` |
| `UnityEngine.ComputeShader` | 12 | `Dispatch`、`FindKernel`、`SetBuffer`、`SetFloat`、`SetInt`、`SetInts`、`SetTexture`、`SetVector` |
| `UnityEngine.CullingGroup` | 11 | `SetBoundingSpheres`、`SetBoundingSphereCount`、`EraseSwapBack`、`QueryIndices`、`IsVisible`、`GetDistance`、`SetBoundingDistances`、`SetDistanceReferencePoint` |
| `UnityEditor.UnityStats` | 8 | `get_batches`、`get_drawCalls`、`get_screenRes`、`get_setPassCalls`、`get_triangles`、`get_usedTextureCount`、`get_usedTextureMemorySize`、`get_vertices` |
| `Unity.Profiling.ProfilerRecorder` | 7 | `Dispose`、`get_CurrentValue`、`get_LastValue`、`get_Valid`、`Start`、`StartNew`、`Stop` |
| `UnityEngine.Camera` | 6 | `get_stereoActiveEye`、`get_stereoEnabled`、`AddCommandBuffer`、`AddCommandBufferAsync`、`GetStereoProjectionMatrix`、`GetStereoViewMatrix` |
| `UnityEngine.Profiling.Profiler` | 6 | `get_enableBinaryLog`、`set_enableBinaryLog`、`get_enabled`、`set_enabled`、`get_logFile`、`set_logFile` |
| `UnityEngine.UI.MaskableGraphic` | 6 | `Cull`、`GetModifiedMaterial`、`RecalculateClipping`、`RecalculateMasking`、`SetClipRect`、`SetClipSoftness` |
| `UnityEngine.GL` | 5 | `End`、`InvalidateState`、`Viewport`、`LoadProjectionMatrix`、`set_sRGBWrite` |
| `UnityEngine.Hash128` | 5 | `CompareTo`、`Equals`、`Append`、`Compute` |
| `UnityEngine.TouchScreenKeyboard` | 5 | `get_isSupported`、`get_status`、`get_text`、`Open`、`set_active` |
| `UnityEngine.Video.VideoPlayer` | 5 | `EnableAudioTrack`、`SetDirectAudioMute`、`SetTargetAudioSource`、`SetDirectAudioVolume`、`set_audioOutputMode` |
| `UnityEditor.EditorWindow` | 4 | `Close`、`GetWindow`、`Show` |
| `UnityEngine.Experimental.Rendering.RayTracingAccelerationStructure` | 4 | `Build`、`GetSize`、`GetInstanceCount` |
| `UnityEngine.GraphicsBuffer` | 4 | `Dispose`、`get_count`、`IsValid`、`Release` |
| `UnityEngine.InputSystem.Utilities.ReadOnlyArray`1` | 4 | `get_Count`、`get_Item`、`System.Collections.Generic.IEnumerable<TValue>.GetEnumerator`、`System.Collections.IEnumerable.GetEnumerator` |
| `UnityEngine.QualitySettings` | 4 | `get_antiAliasing`、`set_globalTextureMipmapLimit`、`set_vSyncCount`、`set_streamingMipmapsActive` |
| `UnityEngine.SceneManagement.SceneManager` | 4 | `get_sceneCount`、`GetSceneAt`、`LoadScene`、`LoadSceneAsync` |
| `UnityEngine.Shader` | 4 | `GetGlobalTexture`、`GetPropertyName`、`GetPropertyType`、`GetPropertyRangeLimits` |
| `UnityEngine.TextCore.LowLevel.FontEngine` | 4 | `SetFaceSize`、`TryGetGlyphIndex`、`TryGetGlyphWithIndexValue`、`TryGetGlyphWithUnicodeValue` |
| `UnityEngine.UI.Graphic` | 4 | `get_rectTransform`、`GraphicUpdateComplete`、`LayoutComplete`、`Rebuild` |
| `UnityEngine.Display` | 3 | `Activate`、`SetParams` |
| `UnityEngine.EventSystems.EventSystem` | 3 | `get_current`、`set_current`、`IsPointerOverGameObject` |
| `UnityEngine.Graphics` | 3 | `DrawTexture`、`ExecuteCommandBuffer`、`ExecuteCommandBufferAsync` |
| `UnityEngine.InputSystem.InputActionMap` | 3 | `get_controlSchemes`、`OnAfterDeserialize`、`OnBeforeSerialize` |
| `UnityEngine.InputSystem.Mouse` | 3 | `OnNextUpdate`、`OnStateEvent`、`ReadValueFromStateIntoBuffer` |
| `UnityEngine.InputSystem.Pointer` | 3 | `OnNextUpdate`、`OnStateEvent`、`ReadValueFromStateIntoBuffer` |
| `UnityEngine.ParticleSystem` | 3 | `RunStopAction`、`UpdateParticles`、`SampleShapeLocal` |
| `UnityEngine.RenderTexture` | 3 | `GetNativeDepthBufferPtr`、`DiscardContents` |
| `UnityEngine.SkinnedMeshRenderer` | 3 | `SetBlendShapeWeight`、`GetVertexBuffer`、`GetPreviousVertexBuffer` |
| `UnityEngine.TestTools.LogAssert` | 3 | `Expect`、`NoUnexpectedReceived` |
| `UnityEngine.Touch` | 3 | `get_fingerId`、`get_phase`、`get_position` |
| `UnityEngine.Animator` | 2 | `Play`、`Update` |
| `UnityEngine.AudioClip` | 2 | `get_isFinite`、`get_isRealtime` |
| `UnityEngine.AudioSource` | 2 | `PlayClipAtPoint`、`ApplySpatialState` |
| `UnityEngine.Input` | 2 | `GetAxis`、`GetTouch` |
| `UnityEngine.Jobs.IJobParallelForTransformExtensions` | 2 | `EarlyJobInit`、`Schedule` |
| `UnityEngine.LineRenderer` | 2 | `Simplify`、`BakeMesh` |
| `UnityEngine.Mesh` | 2 | `Optimize`、`SetIndices` |
| `UnityEngine.ParticleSystemRenderer` | 2 | `SetActiveVertexStreams`、`GetQuadAxes` |
| `UnityEngine.RectTransform` | 2 | `get_pivot`、`get_rect` |
| `UnityEngine.ScreenCapture` | 2 | `CaptureScreenshot`、`WarnIfSuperSized` |
| `UnityEngine.Texture2D` | 2 | `SetPixelData`、`PackTextures` |
| `TMPro.TMP_FontAsset` | 1 | `CreateFontAsset` |
| `Unity.Collections.AllocatorManager+AllocatorHandle` | 1 | `Dispose` |
| `Unity.Collections.AllocatorManager+Block` | 1 | `Dispose` |
| `Unity.Collections.NativeSortExtension` | 1 | `Sort` |
| `Unity.Profiling.Memory.MemoryProfiler` | 1 | `TakeSnapshot` |
| `UnityEngine.AnimationClip` | 1 | `get_length` |
| `UnityEngine.AudioFilterBehaviour` | 1 | `Push` |
| `UnityEngine.AudioSettings` | 1 | `Reset` |
| `UnityEngine.CustomYieldInstruction` | 1 | `Reset` |
| `UnityEngine.EventSystems.UIBehaviour` | 1 | `IsDestroyed` |
| `UnityEngine.InputSystem.Controls.AnyKeyControl` | 1 | `ReadValueFromStateIntoBuffer` |
| `UnityEngine.InputSystem.Controls.AxisControl` | 1 | `ReadValueFromStateIntoBuffer` |
| `UnityEngine.InputSystem.Controls.ButtonControl` | 1 | `ReadValueFromStateIntoBuffer` |
| `UnityEngine.InputSystem.Controls.DeltaControl` | 1 | `ReadValueFromStateIntoBuffer` |
| `UnityEngine.InputSystem.Controls.IntegerControl` | 1 | `ReadValueFromStateIntoBuffer` |
| `UnityEngine.InputSystem.Controls.KeyControl` | 1 | `ReadValueFromStateIntoBuffer` |
| `UnityEngine.InputSystem.Controls.Vector2Control` | 1 | `ReadValueFromStateIntoBuffer` |
| `UnityEngine.InputSystem.InputBinding` | 1 | `Equals` |
| `UnityEngine.InputSystem.InputControl`1` | 1 | `ReadValueFromStateIntoBuffer` |
| `UnityEngine.InputSystem.InputControlScheme` | 1 | `Equals` |
| `UnityEngine.InputSystem.InputDevice` | 1 | `ReadValueFromStateIntoBuffer` |
| `UnityEngine.InputSystem.Keyboard` | 1 | `ReadValueFromStateIntoBuffer` |
| `UnityEngine.InputSystem.LowLevel.DeltaStateEvent` | 1 | `get_typeStatic` |
| `UnityEngine.InputSystem.LowLevel.InputEventListener` | 1 | `Subscribe` |
| `UnityEngine.InputSystem.LowLevel.StateEvent` | 1 | `get_typeStatic` |
| `UnityEngine.InputSystem.Utilities.FourCC` | 1 | `Equals` |
| `UnityEngine.Jobs.TransformAccessArray` | 1 | `Dispose` |
| `UnityEngine.LowLevel.PlayerLoop` | 1 | `SetPlayerLoop` |
| `UnityEngine.Material` | 1 | `SetTexture` |
| `UnityEngine.Motion` | 1 | `get_isLooping` |
| `UnityEngine.Object` | 1 | `set_hideFlags` |
| `UnityEngine.ParticlePhysicsExtensions` | 1 | `GetCollisionEvents` |
| `UnityEngine.RaycastHit` | 1 | `get_textureCoord` |
| `UnityEngine.Renderer` | 1 | `get_bounds` |
| `UnityEngine.Resources` | 1 | `GetBuiltinResource` |
| `UnityEngine.RuntimeAnimatorController` | 1 | `get_animationClips` |
| `UnityEngine.Scripting.GarbageCollector` | 1 | `CollectIncremental` |
| `UnityEngine.Texture2DArray` | 1 | `Apply` |
| `UnityEngine.Texture3D` | 1 | `SetPixelData` |
| `UnityEngine.Time` | 1 | `set_timeScale` |
| `UnityEngine.TrailRenderer` | 1 | `BakeMesh` |
| `UnityEngine.UI.Image` | 1 | `SetNativeSize` |
| `UnityStandardAssets.ImageEffects.PostEffectsBase` | 1 | `DrawBorder` |
| `UnityStubs.Internal.AssetBundleReader` | 1 | `ReadParticleSystem` |

## 完整清单（254 条，按类型分组）

```
UnityStandardAssets.ImageEffects.PostEffectsBase :: DrawBorder
TMPro.TMP_FontAsset :: CreateFontAsset
UnityStubs.Internal.AssetBundleReader :: ReadParticleSystem
UnityEditor.EditorWindow :: Close
UnityEditor.EditorWindow :: GetWindow
UnityEditor.EditorWindow :: GetWindow
UnityEditor.EditorWindow :: Show
UnityEditor.UnityStats :: get_batches
UnityEditor.UnityStats :: get_drawCalls
UnityEditor.UnityStats :: get_screenRes
UnityEditor.UnityStats :: get_setPassCalls
UnityEditor.UnityStats :: get_triangles
UnityEditor.UnityStats :: get_usedTextureCount
UnityEditor.UnityStats :: get_usedTextureMemorySize
UnityEditor.UnityStats :: get_vertices
Unity.Profiling.ProfilerRecorder :: Dispose
Unity.Profiling.ProfilerRecorder :: get_CurrentValue
Unity.Profiling.ProfilerRecorder :: get_LastValue
Unity.Profiling.ProfilerRecorder :: get_Valid
Unity.Profiling.ProfilerRecorder :: Start
Unity.Profiling.ProfilerRecorder :: StartNew
Unity.Profiling.ProfilerRecorder :: Stop
Unity.Profiling.Memory.MemoryProfiler :: TakeSnapshot
Unity.Collections.NativeSortExtension :: Sort
UnityEngine.AnimationClip :: get_length
UnityEngine.RuntimeAnimatorController :: get_animationClips
UnityEngine.Animator :: Play
UnityEngine.Animator :: Update
UnityEngine.AudioClip :: get_isFinite
UnityEngine.AudioClip :: get_isRealtime
UnityEngine.AudioFilterBehaviour :: Push
UnityEngine.AudioSettings :: Reset
UnityEngine.AudioSource :: PlayClipAtPoint
UnityEngine.AudioSource :: ApplySpatialState
UnityEngine.Camera :: get_stereoActiveEye
UnityEngine.Camera :: get_stereoEnabled
UnityEngine.Camera :: AddCommandBuffer
UnityEngine.Camera :: AddCommandBufferAsync
UnityEngine.Camera :: GetStereoProjectionMatrix
UnityEngine.Camera :: GetStereoViewMatrix
UnityEngine.ComputeShader :: Dispatch
UnityEngine.ComputeShader :: FindKernel
UnityEngine.ComputeShader :: SetBuffer
UnityEngine.ComputeShader :: SetBuffer
UnityEngine.ComputeShader :: SetFloat
UnityEngine.ComputeShader :: SetInt
UnityEngine.ComputeShader :: SetInts
UnityEngine.ComputeShader :: SetInts
UnityEngine.ComputeShader :: SetTexture
UnityEngine.ComputeShader :: SetTexture
UnityEngine.ComputeShader :: SetTexture
UnityEngine.ComputeShader :: SetVector
UnityEngine.CullingGroup :: SetBoundingSpheres
UnityEngine.CullingGroup :: SetBoundingSphereCount
UnityEngine.CullingGroup :: EraseSwapBack
UnityEngine.CullingGroup :: QueryIndices
UnityEngine.CullingGroup :: QueryIndices
UnityEngine.CullingGroup :: QueryIndices
UnityEngine.CullingGroup :: IsVisible
UnityEngine.CullingGroup :: GetDistance
UnityEngine.CullingGroup :: SetBoundingDistances
UnityEngine.CullingGroup :: SetDistanceReferencePoint
UnityEngine.CullingGroup :: SetDistanceReferencePoint
UnityEngine.CustomYieldInstruction :: Reset
UnityEngine.Display :: Activate
UnityEngine.Display :: Activate
UnityEngine.Display :: SetParams
UnityEngine.GL :: End
UnityEngine.GL :: InvalidateState
UnityEngine.GL :: Viewport
UnityEngine.GL :: LoadProjectionMatrix
UnityEngine.GL :: set_sRGBWrite
UnityEngine.Graphics :: DrawTexture
UnityEngine.Graphics :: ExecuteCommandBuffer
UnityEngine.Graphics :: ExecuteCommandBufferAsync
UnityEngine.GraphicsBuffer :: Dispose
UnityEngine.GraphicsBuffer :: get_count
UnityEngine.GraphicsBuffer :: IsValid
UnityEngine.GraphicsBuffer :: Release
UnityEngine.Hash128 :: CompareTo
UnityEngine.Hash128 :: CompareTo
UnityEngine.Hash128 :: Equals
UnityEngine.Hash128 :: Append
UnityEngine.Hash128 :: Compute
UnityEngine.Input :: GetAxis
UnityEngine.Input :: GetTouch
UnityEngine.LineRenderer :: Simplify
UnityEngine.LineRenderer :: BakeMesh
UnityEngine.Material :: SetTexture
UnityEngine.Mesh :: Optimize
UnityEngine.Mesh :: SetIndices
UnityEngine.Motion :: get_isLooping
UnityEngine.Object :: set_hideFlags
UnityEngine.ParticlePhysicsExtensions :: GetCollisionEvents
UnityEngine.ParticleSystem :: RunStopAction
UnityEngine.ParticleSystem :: UpdateParticles
UnityEngine.ParticleSystem :: SampleShapeLocal
UnityEngine.ParticleSystemRenderer :: SetActiveVertexStreams
UnityEngine.ParticleSystemRenderer :: GetQuadAxes
UnityEngine.QualitySettings :: get_antiAliasing
UnityEngine.QualitySettings :: set_globalTextureMipmapLimit
UnityEngine.QualitySettings :: set_vSyncCount
UnityEngine.QualitySettings :: set_streamingMipmapsActive
UnityEngine.RaycastHit :: get_textureCoord
UnityEngine.RectTransform :: get_pivot
UnityEngine.RectTransform :: get_rect
UnityEngine.Renderer :: get_bounds
UnityEngine.RenderTexture :: GetNativeDepthBufferPtr
UnityEngine.RenderTexture :: DiscardContents
UnityEngine.RenderTexture :: DiscardContents
UnityEngine.Resources :: GetBuiltinResource
UnityEngine.ScreenCapture :: CaptureScreenshot
UnityEngine.ScreenCapture :: WarnIfSuperSized
UnityEngine.Shader :: GetGlobalTexture
UnityEngine.Shader :: GetPropertyName
UnityEngine.Shader :: GetPropertyType
UnityEngine.Shader :: GetPropertyRangeLimits
UnityEngine.SkinnedMeshRenderer :: SetBlendShapeWeight
UnityEngine.SkinnedMeshRenderer :: GetVertexBuffer
UnityEngine.SkinnedMeshRenderer :: GetPreviousVertexBuffer
UnityEngine.Texture2D :: SetPixelData
UnityEngine.Texture2D :: PackTextures
UnityEngine.Texture2DArray :: Apply
UnityEngine.Texture3D :: SetPixelData
UnityEngine.Time :: set_timeScale
UnityEngine.Touch :: get_fingerId
UnityEngine.Touch :: get_phase
UnityEngine.Touch :: get_position
UnityEngine.TouchScreenKeyboard :: get_isSupported
UnityEngine.TouchScreenKeyboard :: get_status
UnityEngine.TouchScreenKeyboard :: get_text
UnityEngine.TouchScreenKeyboard :: Open
UnityEngine.TouchScreenKeyboard :: set_active
UnityEngine.TrailRenderer :: BakeMesh
UnityEngine.Video.VideoPlayer :: EnableAudioTrack
UnityEngine.Video.VideoPlayer :: SetDirectAudioMute
UnityEngine.Video.VideoPlayer :: SetTargetAudioSource
UnityEngine.Video.VideoPlayer :: SetDirectAudioVolume
UnityEngine.Video.VideoPlayer :: set_audioOutputMode
UnityEngine.TestTools.LogAssert :: Expect
UnityEngine.TestTools.LogAssert :: Expect
UnityEngine.TestTools.LogAssert :: NoUnexpectedReceived
UnityEngine.TextCore.LowLevel.FontEngine :: SetFaceSize
UnityEngine.TextCore.LowLevel.FontEngine :: TryGetGlyphIndex
UnityEngine.TextCore.LowLevel.FontEngine :: TryGetGlyphWithIndexValue
UnityEngine.TextCore.LowLevel.FontEngine :: TryGetGlyphWithUnicodeValue
UnityEngine.Profiling.Profiler :: get_enableBinaryLog
UnityEngine.Profiling.Profiler :: set_enableBinaryLog
UnityEngine.Profiling.Profiler :: get_enabled
UnityEngine.Profiling.Profiler :: set_enabled
UnityEngine.Profiling.Profiler :: get_logFile
UnityEngine.Profiling.Profiler :: set_logFile
UnityEngine.LowLevel.PlayerLoop :: SetPlayerLoop
UnityEngine.SceneManagement.SceneManager :: get_sceneCount
UnityEngine.SceneManagement.SceneManager :: GetSceneAt
UnityEngine.SceneManagement.SceneManager :: LoadScene
UnityEngine.SceneManagement.SceneManager :: LoadSceneAsync
UnityEngine.Jobs.IJobParallelForTransformExtensions :: EarlyJobInit
UnityEngine.Jobs.IJobParallelForTransformExtensions :: Schedule
UnityEngine.Jobs.TransformAccessArray :: Dispose
UnityEngine.Experimental.Rendering.RayTracingAccelerationStructure :: Build
UnityEngine.Experimental.Rendering.RayTracingAccelerationStructure :: Build
UnityEngine.Experimental.Rendering.RayTracingAccelerationStructure :: GetSize
UnityEngine.Experimental.Rendering.RayTracingAccelerationStructure :: GetInstanceCount
UnityEngine.Scripting.GarbageCollector :: CollectIncremental
UnityEngine.EventSystems.EventSystem :: get_current
UnityEngine.EventSystems.EventSystem :: set_current
UnityEngine.EventSystems.EventSystem :: IsPointerOverGameObject
UnityEngine.EventSystems.UIBehaviour :: IsDestroyed
UnityEngine.UI.Graphic :: get_rectTransform
UnityEngine.UI.Graphic :: GraphicUpdateComplete
UnityEngine.UI.Graphic :: LayoutComplete
UnityEngine.UI.Graphic :: Rebuild
UnityEngine.UI.Image :: SetNativeSize
UnityEngine.UI.MaskableGraphic :: Cull
UnityEngine.UI.MaskableGraphic :: GetModifiedMaterial
UnityEngine.UI.MaskableGraphic :: RecalculateClipping
UnityEngine.UI.MaskableGraphic :: RecalculateMasking
UnityEngine.UI.MaskableGraphic :: SetClipRect
UnityEngine.UI.MaskableGraphic :: SetClipSoftness
UnityEngine.Rendering.CommandBuffer :: EnableScissorRect
UnityEngine.Rendering.CommandBuffer :: DisableScissorRect
UnityEngine.Rendering.CommandBuffer :: Clear
UnityEngine.Rendering.CommandBuffer :: ClearRenderTarget
UnityEngine.Rendering.CommandBuffer :: ClearRenderTarget
UnityEngine.Rendering.CommandBuffer :: ClearRenderTarget
UnityEngine.Rendering.CommandBuffer :: DispatchCompute
UnityEngine.Rendering.CommandBuffer :: DrawMesh
UnityEngine.Rendering.CommandBuffer :: DrawMesh
UnityEngine.Rendering.CommandBuffer :: DrawMesh
UnityEngine.Rendering.CommandBuffer :: SetViewProjectionMatrices
UnityEngine.Rendering.CommandBuffer :: SetViewport
UnityEngine.Rendering.CommandBuffer :: Blit
UnityEngine.Rendering.CommandBuffer :: Blit
UnityEngine.Rendering.CommandBuffer :: Blit
UnityEngine.Rendering.CommandBuffer :: GetTemporaryRT
UnityEngine.Rendering.CommandBuffer :: GetTemporaryRT
UnityEngine.Rendering.CommandBuffer :: GetTemporaryRT
UnityEngine.Rendering.CommandBuffer :: GetTemporaryRT
UnityEngine.Rendering.CommandBuffer :: ReleaseTemporaryRT
UnityEngine.Rendering.CommandBuffer :: SetGlobalTexture
UnityEngine.Rendering.CommandBuffer :: SetGlobalTexture
UnityEngine.Rendering.CommandBuffer :: SetRenderTarget
UnityEngine.Rendering.CommandBuffer :: IssuePluginEvent
UnityEngine.Rendering.CommandBuffer :: IssuePluginEventAndData
UnityEngine.Rendering.CommandBuffer :: IssuePluginEventAndDataWithFlags
UnityEngine.Rendering.CommandBuffer :: SetBufferData
UnityEngine.Rendering.CommandBuffer :: SetComputeIntParam
UnityEngine.Rendering.CommandBuffer :: SetExecutionFlags
UnityEngine.Rendering.CommandBuffer :: SetRenderTarget
UnityEngine.InputSystem.InputActionAsset :: Contains
UnityEngine.InputSystem.InputActionAsset :: Disable
UnityEngine.InputSystem.InputActionAsset :: Enable
UnityEngine.InputSystem.InputActionAsset :: FindAction
UnityEngine.InputSystem.InputActionAsset :: get_bindingMask
UnityEngine.InputSystem.InputActionAsset :: set_bindingMask
UnityEngine.InputSystem.InputActionAsset :: get_bindings
UnityEngine.InputSystem.InputActionAsset :: get_controlSchemes
UnityEngine.InputSystem.InputActionAsset :: get_devices
UnityEngine.InputSystem.InputActionAsset :: set_devices
UnityEngine.InputSystem.InputActionAsset :: GetEnumerator
UnityEngine.InputSystem.InputActionAsset :: FindActionMap
UnityEngine.InputSystem.InputActionAsset :: System.Collections.IEnumerable.GetEnumerator
UnityEngine.InputSystem.InputActionMap :: get_controlSchemes
UnityEngine.InputSystem.InputActionMap :: OnAfterDeserialize
UnityEngine.InputSystem.InputActionMap :: OnBeforeSerialize
UnityEngine.InputSystem.InputBinding :: Equals
UnityEngine.InputSystem.InputControlScheme :: Equals
UnityEngine.InputSystem.InputDevice :: ReadValueFromStateIntoBuffer
UnityEngine.InputSystem.Keyboard :: ReadValueFromStateIntoBuffer
UnityEngine.InputSystem.Mouse :: OnNextUpdate
UnityEngine.InputSystem.Mouse :: OnStateEvent
UnityEngine.InputSystem.Mouse :: ReadValueFromStateIntoBuffer
UnityEngine.InputSystem.Pointer :: OnNextUpdate
UnityEngine.InputSystem.Pointer :: OnStateEvent
UnityEngine.InputSystem.Pointer :: ReadValueFromStateIntoBuffer
UnityEngine.InputSystem.InputControl`1 :: ReadValueFromStateIntoBuffer
UnityEngine.InputSystem.Utilities.FourCC :: Equals
UnityEngine.InputSystem.Utilities.ReadOnlyArray`1 :: get_Count
UnityEngine.InputSystem.Utilities.ReadOnlyArray`1 :: get_Item
UnityEngine.InputSystem.Utilities.ReadOnlyArray`1 :: System.Collections.Generic.IEnumerable<TValue>.GetEnumerator
UnityEngine.InputSystem.Utilities.ReadOnlyArray`1 :: System.Collections.IEnumerable.GetEnumerator
UnityEngine.InputSystem.LowLevel.DeltaStateEvent :: get_typeStatic
UnityEngine.InputSystem.LowLevel.InputEventListener :: Subscribe
UnityEngine.InputSystem.LowLevel.StateEvent :: get_typeStatic
UnityEngine.InputSystem.Controls.AnyKeyControl :: ReadValueFromStateIntoBuffer
UnityEngine.InputSystem.Controls.AxisControl :: ReadValueFromStateIntoBuffer
UnityEngine.InputSystem.Controls.ButtonControl :: ReadValueFromStateIntoBuffer
UnityEngine.InputSystem.Controls.DeltaControl :: ReadValueFromStateIntoBuffer
UnityEngine.InputSystem.Controls.IntegerControl :: ReadValueFromStateIntoBuffer
UnityEngine.InputSystem.Controls.KeyControl :: ReadValueFromStateIntoBuffer
UnityEngine.InputSystem.Controls.Vector2Control :: ReadValueFromStateIntoBuffer
Unity.Collections.AllocatorManager+Block :: Dispose
Unity.Collections.AllocatorManager+AllocatorHandle :: Dispose
```

## 展开签名（288 条：每个「类型 :: 成员名」的全部同名重载）

```csharp
TMPro.TMP_FontAsset :: static TMP_FontAsset CreateFontAsset(Font font)
TMPro.TMP_FontAsset :: static TMP_FontAsset CreateFontAsset(Font font, Int32 samplingPointSize, Int32 atlasPadding, GlyphRenderMode renderMode, Int32 atlasWidth, Int32 atlasHeight, AtlasPopulationMode atlasPopulationMode, Boolean enableMultiAtlasSupport)
Unity.Collections.AllocatorManager+AllocatorHandle :: Void Dispose()
Unity.Collections.AllocatorManager+Block :: Void Dispose()
Unity.Collections.NativeSortExtension :: static Void Sort(NativeList`1 list, T1 comp)
Unity.Profiling.Memory.MemoryProfiler :: static Void TakeSnapshot(String path, Action`2 finishCallback, CaptureFlags captureFlags)
Unity.Profiling.ProfilerRecorder :: Void Dispose()
Unity.Profiling.ProfilerRecorder :: Int64 get_CurrentValue()
Unity.Profiling.ProfilerRecorder :: Int64 get_LastValue()
Unity.Profiling.ProfilerRecorder :: Boolean get_Valid()
Unity.Profiling.ProfilerRecorder :: Void Start()
Unity.Profiling.ProfilerRecorder :: static ProfilerRecorder StartNew(ProfilerCategory category, String statName, Int32 capacity, ProfilerRecorderOptions options)
Unity.Profiling.ProfilerRecorder :: Void Stop()
UnityEditor.EditorWindow :: Void Close()
UnityEditor.EditorWindow :: static EditorWindow GetWindow(Type p0)
UnityEditor.EditorWindow :: static T0 GetWindow(String p0)
UnityEditor.EditorWindow :: Void Show()
UnityEditor.UnityStats :: static Int32 get_batches()
UnityEditor.UnityStats :: static Int32 get_drawCalls()
UnityEditor.UnityStats :: static String get_screenRes()
UnityEditor.UnityStats :: static Int32 get_setPassCalls()
UnityEditor.UnityStats :: static Int32 get_triangles()
UnityEditor.UnityStats :: static Int32 get_usedTextureCount()
UnityEditor.UnityStats :: static Int32 get_usedTextureMemorySize()
UnityEditor.UnityStats :: static Int32 get_vertices()
UnityEngine.AnimationClip :: Single get_length()
UnityEngine.Animator :: Void Play(String stateName)
UnityEngine.Animator :: Void Play(String stateName, Int32 layer)
UnityEngine.Animator :: Void Play(String stateName, Int32 layer, Single normalizedTime)
UnityEngine.Animator :: Void Update(Single deltaTime)
UnityEngine.AudioClip :: Boolean get_isFinite()
UnityEngine.AudioClip :: Boolean get_isRealtime()
UnityEngine.AudioFilterBehaviour :: Void Push()
UnityEngine.AudioSettings :: static Boolean Reset(AudioConfiguration config)
UnityEngine.AudioSource :: Void ApplySpatialState()
UnityEngine.AudioSource :: static Void PlayClipAtPoint(AudioClip clip, Vector3 position, Single volume)
UnityEngine.Camera :: Void AddCommandBuffer(CameraEvent evt, CommandBuffer buffer)
UnityEngine.Camera :: Void AddCommandBufferAsync(CameraEvent evt, CommandBuffer buffer, ComputeQueueType queueType)
UnityEngine.Camera :: MonoOrStereoscopicEye get_stereoActiveEye()
UnityEngine.Camera :: Boolean get_stereoEnabled()
UnityEngine.Camera :: Matrix4x4 GetStereoProjectionMatrix(StereoscopicEye eye)
UnityEngine.Camera :: Matrix4x4 GetStereoViewMatrix(StereoscopicEye eye)
UnityEngine.ComputeShader :: Void Dispatch(Int32 kernelIndex, Int32 threadGroupsX, Int32 threadGroupsY, Int32 threadGroupsZ)
UnityEngine.ComputeShader :: Int32 FindKernel(String name)
UnityEngine.ComputeShader :: Void SetBuffer(Int32 kernelIndex, Int32 nameID, GraphicsBuffer buffer)
UnityEngine.ComputeShader :: Void SetBuffer(Int32 kernelIndex, String name, ComputeBuffer buffer)
UnityEngine.ComputeShader :: Void SetFloat(String name, Single val)
UnityEngine.ComputeShader :: Void SetInt(String name, Int32 val)
UnityEngine.ComputeShader :: Void SetInts(Int32 nameID, Int32[] values)
UnityEngine.ComputeShader :: Void SetInts(String name, Int32[] values)
UnityEngine.ComputeShader :: Void SetTexture(Int32 kernelIndex, String name, Texture texture)
UnityEngine.ComputeShader :: Void SetTexture(Int32 kernelIndex, Int32 nameID, Texture texture)
UnityEngine.ComputeShader :: Void SetTexture(Int32 kernelIndex, String name, Texture texture, Int32 mipLevel)
UnityEngine.ComputeShader :: Void SetVector(String name, Vector4 val)
UnityEngine.CullingGroup :: Void EraseSwapBack(Int32 index)
UnityEngine.CullingGroup :: Int32 GetDistance(Int32 index)
UnityEngine.CullingGroup :: Boolean IsVisible(Int32 index)
UnityEngine.CullingGroup :: Int32 QueryIndices(Boolean visible, Int32[] result, Int32 firstIndex)
UnityEngine.CullingGroup :: Int32 QueryIndices(Int32 distanceIndex, Int32[] result, Int32 firstIndex)
UnityEngine.CullingGroup :: Int32 QueryIndices(Boolean visible, Int32 distanceIndex, Int32[] result, Int32 firstIndex)
UnityEngine.CullingGroup :: Void SetBoundingDistances(Single[] distances)
UnityEngine.CullingGroup :: Void SetBoundingSphereCount(Int32 count)
UnityEngine.CullingGroup :: Void SetBoundingSpheres(BoundingSphere[] array)
UnityEngine.CullingGroup :: Void SetDistanceReferencePoint(Vector3 point)
UnityEngine.CullingGroup :: Void SetDistanceReferencePoint(Transform transform)
UnityEngine.CustomYieldInstruction :: Void Reset()
UnityEngine.Display :: Void Activate()
UnityEngine.Display :: Void Activate(Int32 width, Int32 height, RefreshRate refreshRate)
UnityEngine.Display :: Void Activate(Int32 width, Int32 height, Int32 refreshRate)
UnityEngine.Display :: Void SetParams(Int32 width, Int32 height, Int32 x, Int32 y)
UnityEngine.EventSystems.EventSystem :: static EventSystem get_current()
UnityEngine.EventSystems.EventSystem :: Boolean IsPointerOverGameObject()
UnityEngine.EventSystems.EventSystem :: static Void set_current(EventSystem value)
UnityEngine.EventSystems.UIBehaviour :: Boolean IsDestroyed()
UnityEngine.Experimental.Rendering.RayTracingAccelerationStructure :: Void Build()
UnityEngine.Experimental.Rendering.RayTracingAccelerationStructure :: Void Build(Vector3 relativeOrigin)
UnityEngine.Experimental.Rendering.RayTracingAccelerationStructure :: UInt32 GetInstanceCount()
UnityEngine.Experimental.Rendering.RayTracingAccelerationStructure :: UInt64 GetSize()
UnityEngine.GL :: static Void End()
UnityEngine.GL :: static Void InvalidateState()
UnityEngine.GL :: static Void LoadProjectionMatrix(Matrix4x4 mat)
UnityEngine.GL :: static Void set_sRGBWrite(Boolean value)
UnityEngine.GL :: static Void Viewport(Rect pixelRect)
UnityEngine.Graphics :: static Void DrawTexture(Rect screenRect, Texture texture)
UnityEngine.Graphics :: static Void DrawTexture(Rect screenRect, Texture texture, Rect sourceRect, Int32 leftBorder, Int32 rightBorder, Int32 topBorder, Int32 bottomBorder)
UnityEngine.Graphics :: static Void DrawTexture(Rect screenRect, Texture texture, Rect sourceRect, Int32 leftBorder, Int32 rightBorder, Int32 topBorder, Int32 bottomBorder, Color color)
UnityEngine.Graphics :: static Void DrawTexture(Rect screenRect, Texture texture, Rect sourceRect, Int32 leftBorder, Int32 rightBorder, Int32 topBorder, Int32 bottomBorder, Material mat, Int32 pass)
UnityEngine.Graphics :: static Void DrawTexture(Rect screenRect, Texture texture, Rect sourceRect, Int32 leftBorder, Int32 rightBorder, Int32 topBorder, Int32 bottomBorder, Color color, Material mat)
UnityEngine.Graphics :: static Void DrawTexture(Rect screenRect, Texture texture, Rect sourceRect, Int32 leftBorder, Int32 rightBorder, Int32 topBorder, Int32 bottomBorder, Material mat)
UnityEngine.Graphics :: static Void DrawTexture(Rect screenRect, Texture texture, Int32 leftBorder, Int32 rightBorder, Int32 topBorder, Int32 bottomBorder)
UnityEngine.Graphics :: static Void DrawTexture(Rect screenRect, Texture texture, Int32 leftBorder, Int32 rightBorder, Int32 topBorder, Int32 bottomBorder, Material mat)
UnityEngine.Graphics :: static Void DrawTexture(Rect screenRect, Texture texture, Int32 leftBorder, Int32 rightBorder, Int32 topBorder, Int32 bottomBorder, Material mat, Int32 pass)
UnityEngine.Graphics :: static Void DrawTexture(Rect screenRect, Texture texture, Material mat)
UnityEngine.Graphics :: static Void DrawTexture(Rect screenRect, Texture texture, Material mat, Int32 pass)
UnityEngine.Graphics :: static Void DrawTexture(Rect screenRect, Texture texture, Rect sourceRect, Int32 leftBorder, Int32 rightBorder, Int32 topBorder, Int32 bottomBorder, Color color, Material mat, Int32 pass)
UnityEngine.Graphics :: static Void ExecuteCommandBuffer(CommandBuffer buffer)
UnityEngine.Graphics :: static Void ExecuteCommandBufferAsync(CommandBuffer buffer, ComputeQueueType queueType)
UnityEngine.GraphicsBuffer :: Void Dispose()
UnityEngine.GraphicsBuffer :: Int32 get_count()
UnityEngine.GraphicsBuffer :: Boolean IsValid()
UnityEngine.GraphicsBuffer :: Void Release()
UnityEngine.Hash128 :: Void Append(T0[] data)
UnityEngine.Hash128 :: Int32 CompareTo(Object obj)
UnityEngine.Hash128 :: Int32 CompareTo(Hash128 rhs)
UnityEngine.Hash128 :: static Hash128 Compute(Int32 val)
UnityEngine.Hash128 :: Boolean Equals(Hash128 obj)
UnityEngine.Input :: static Single GetAxis(String axisName)
UnityEngine.Input :: static Touch GetTouch(Int32 index)
UnityEngine.InputSystem.Controls.AnyKeyControl :: Void ReadValueFromStateIntoBuffer(Void* statePtr, Void* bufferPtr, Int32 bufferSize)
UnityEngine.InputSystem.Controls.AxisControl :: Void ReadValueFromStateIntoBuffer(Void* statePtr, Void* bufferPtr, Int32 bufferSize)
UnityEngine.InputSystem.Controls.ButtonControl :: Void ReadValueFromStateIntoBuffer(Void* statePtr, Void* bufferPtr, Int32 bufferSize)
UnityEngine.InputSystem.Controls.DeltaControl :: Void ReadValueFromStateIntoBuffer(Void* statePtr, Void* bufferPtr, Int32 bufferSize)
UnityEngine.InputSystem.Controls.IntegerControl :: Void ReadValueFromStateIntoBuffer(Void* statePtr, Void* bufferPtr, Int32 bufferSize)
UnityEngine.InputSystem.Controls.KeyControl :: Void ReadValueFromStateIntoBuffer(Void* statePtr, Void* bufferPtr, Int32 bufferSize)
UnityEngine.InputSystem.Controls.Vector2Control :: Void ReadValueFromStateIntoBuffer(Void* statePtr, Void* bufferPtr, Int32 bufferSize)
UnityEngine.InputSystem.InputActionAsset :: Boolean Contains(InputAction action)
UnityEngine.InputSystem.InputActionAsset :: Void Disable()
UnityEngine.InputSystem.InputActionAsset :: Void Enable()
UnityEngine.InputSystem.InputActionAsset :: InputAction FindAction(String actionNameOrId, Boolean throwIfNotFound)
UnityEngine.InputSystem.InputActionAsset :: InputActionMap FindActionMap(String nameOrId, Boolean throwIfNotFound)
UnityEngine.InputSystem.InputActionAsset :: Nullable`1 get_bindingMask()
UnityEngine.InputSystem.InputActionAsset :: IEnumerable`1 get_bindings()
UnityEngine.InputSystem.InputActionAsset :: ReadOnlyArray`1 get_controlSchemes()
UnityEngine.InputSystem.InputActionAsset :: Nullable`1 get_devices()
UnityEngine.InputSystem.InputActionAsset :: IEnumerator`1 GetEnumerator()
UnityEngine.InputSystem.InputActionAsset :: Void set_bindingMask(Nullable`1 value)
UnityEngine.InputSystem.InputActionAsset :: Void set_devices(Nullable`1 value)
UnityEngine.InputSystem.InputActionAsset :: IEnumerator System.Collections.IEnumerable.GetEnumerator()
UnityEngine.InputSystem.InputActionMap :: ReadOnlyArray`1 get_controlSchemes()
UnityEngine.InputSystem.InputActionMap :: Void OnAfterDeserialize()
UnityEngine.InputSystem.InputActionMap :: Void OnBeforeSerialize()
UnityEngine.InputSystem.InputBinding :: Boolean Equals(InputBinding other)
UnityEngine.InputSystem.InputControl`1 :: Void ReadValueFromStateIntoBuffer(Void* statePtr, Void* bufferPtr, Int32 bufferSize)
UnityEngine.InputSystem.InputControlScheme :: Boolean Equals(InputControlScheme other)
UnityEngine.InputSystem.InputDevice :: Void ReadValueFromStateIntoBuffer(Void* statePtr, Void* bufferPtr, Int32 bufferSize)
UnityEngine.InputSystem.Keyboard :: Void ReadValueFromStateIntoBuffer(Void* statePtr, Void* bufferPtr, Int32 bufferSize)
UnityEngine.InputSystem.LowLevel.DeltaStateEvent :: FourCC get_typeStatic()
UnityEngine.InputSystem.LowLevel.InputEventListener :: IDisposable Subscribe(IObserver`1 observer)
UnityEngine.InputSystem.LowLevel.StateEvent :: FourCC get_typeStatic()
UnityEngine.InputSystem.Mouse :: Void OnNextUpdate()
UnityEngine.InputSystem.Mouse :: Void OnStateEvent(InputEventPtr eventPtr)
UnityEngine.InputSystem.Mouse :: Void ReadValueFromStateIntoBuffer(Void* statePtr, Void* bufferPtr, Int32 bufferSize)
UnityEngine.InputSystem.Pointer :: Void OnNextUpdate()
UnityEngine.InputSystem.Pointer :: Void OnStateEvent(InputEventPtr eventPtr)
UnityEngine.InputSystem.Pointer :: Void ReadValueFromStateIntoBuffer(Void* statePtr, Void* bufferPtr, Int32 bufferSize)
UnityEngine.InputSystem.Utilities.FourCC :: Boolean Equals(FourCC other)
UnityEngine.InputSystem.Utilities.ReadOnlyArray`1 :: Int32 get_Count()
UnityEngine.InputSystem.Utilities.ReadOnlyArray`1 :: TValue get_Item(Int32 index)
UnityEngine.InputSystem.Utilities.ReadOnlyArray`1 :: IEnumerator`1 System.Collections.Generic.IEnumerable<TValue>.GetEnumerator()
UnityEngine.InputSystem.Utilities.ReadOnlyArray`1 :: IEnumerator System.Collections.IEnumerable.GetEnumerator()
UnityEngine.Jobs.IJobParallelForTransformExtensions :: static Void EarlyJobInit()
UnityEngine.Jobs.IJobParallelForTransformExtensions :: static JobHandle Schedule(T0 jobData, TransformAccessArray transforms, JobHandle dependsOn)
UnityEngine.Jobs.TransformAccessArray :: Void Dispose()
UnityEngine.LineRenderer :: Void BakeMesh(Mesh mesh, Boolean useTransform)
UnityEngine.LineRenderer :: Void BakeMesh(Mesh mesh, Camera camera, Boolean useTransform)
UnityEngine.LineRenderer :: Void Simplify(Single tolerance)
UnityEngine.LowLevel.PlayerLoop :: static Void SetPlayerLoop(PlayerLoopSystem loop)
UnityEngine.Material :: Void SetTexture(Int32 nameID, Texture value)
UnityEngine.Material :: Void SetTexture(String name, Texture value)
UnityEngine.Material :: Void SetTexture(Int32 nameID, RenderTexture value, RenderTextureSubElement element)
UnityEngine.Material :: Void SetTexture(String name, RenderTexture value, RenderTextureSubElement element)
UnityEngine.Mesh :: Void Optimize()
UnityEngine.Mesh :: Void SetIndices(Int32[] indices, MeshTopology topology, Int32 submesh)
UnityEngine.Mesh :: Void SetIndices(Int32[] indices, MeshTopology topology, Int32 submesh, Boolean calculateBounds, Int32 baseVertex)
UnityEngine.Mesh :: Void SetIndices(List`1 indices, MeshTopology topology, Int32 submesh, Boolean calculateBounds, Int32 baseVertex)
UnityEngine.Mesh :: Void SetIndices(List`1 indices, MeshTopology topology, Int32 submesh, Boolean calculateBounds, Int32 baseVertex)
UnityEngine.Motion :: Boolean get_isLooping()
UnityEngine.Object :: Void set_hideFlags(HideFlags value)
UnityEngine.ParticlePhysicsExtensions :: static Int32 GetCollisionEvents(ParticleSystem ps, GameObject go, List`1 collisionEvents)
UnityEngine.ParticleSystem :: Void RunStopAction()
UnityEngine.ParticleSystem :: Boolean SampleShapeLocal(ShapeState shape, Vector3& position, Vector3& direction)
UnityEngine.ParticleSystem :: Void UpdateParticles(Single dt)
UnityEngine.ParticleSystemRenderer :: Void GetQuadAxes(ParticleSystem system, Quaternion viewRotation, Vector3& right, Vector3& up)
UnityEngine.ParticleSystemRenderer :: Void SetActiveVertexStreams(List`1 streams)
UnityEngine.Profiling.Profiler :: static Boolean get_enableBinaryLog()
UnityEngine.Profiling.Profiler :: static Boolean get_enabled()
UnityEngine.Profiling.Profiler :: static String get_logFile()
UnityEngine.Profiling.Profiler :: static Void set_enableBinaryLog(Boolean value)
UnityEngine.Profiling.Profiler :: static Void set_enabled(Boolean value)
UnityEngine.Profiling.Profiler :: static Void set_logFile(String value)
UnityEngine.QualitySettings :: static Int32 get_antiAliasing()
UnityEngine.QualitySettings :: static Void set_globalTextureMipmapLimit(Int32 value)
UnityEngine.QualitySettings :: static Void set_streamingMipmapsActive(Boolean value)
UnityEngine.QualitySettings :: static Void set_vSyncCount(Int32 value)
UnityEngine.RaycastHit :: Vector2 get_textureCoord()
UnityEngine.RectTransform :: Vector2 get_pivot()
UnityEngine.RectTransform :: Rect get_rect()
UnityEngine.Renderer :: Bounds get_bounds()
UnityEngine.Rendering.CommandBuffer :: Void Blit(RenderTargetIdentifier source, RenderTargetIdentifier dest)
UnityEngine.Rendering.CommandBuffer :: Void Blit(RenderTargetIdentifier source, RenderTargetIdentifier dest, Material mat)
UnityEngine.Rendering.CommandBuffer :: Void Blit(RenderTargetIdentifier source, RenderTargetIdentifier dest, Material mat, Int32 pass)
UnityEngine.Rendering.CommandBuffer :: Void Clear()
UnityEngine.Rendering.CommandBuffer :: Void ClearRenderTarget(Boolean clearDepth, Boolean clearColor, Color backgroundColor)
UnityEngine.Rendering.CommandBuffer :: Void ClearRenderTarget(RTClearFlags clearFlags, Color backgroundColor, Single depth, UInt32 stencil)
UnityEngine.Rendering.CommandBuffer :: Void ClearRenderTarget(Boolean clearDepth, Boolean clearColor, Color backgroundColor, Single depth)
UnityEngine.Rendering.CommandBuffer :: Void DisableScissorRect()
UnityEngine.Rendering.CommandBuffer :: Void DispatchCompute(ComputeShader computeShader, Int32 kernelIndex, Int32 threadGroupsX, Int32 threadGroupsY, Int32 threadGroupsZ)
UnityEngine.Rendering.CommandBuffer :: Void DrawMesh(Mesh mesh, Matrix4x4 matrix, Material material)
UnityEngine.Rendering.CommandBuffer :: Void DrawMesh(Mesh mesh, Matrix4x4 matrix, Material material, Int32 submeshIndex, Int32 shaderPass)
UnityEngine.Rendering.CommandBuffer :: Void DrawMesh(Mesh mesh, Matrix4x4 matrix, Material material, Int32 submeshIndex, Int32 shaderPass, MaterialPropertyBlock properties)
UnityEngine.Rendering.CommandBuffer :: Void EnableScissorRect(Rect scissor)
UnityEngine.Rendering.CommandBuffer :: Void GetTemporaryRT(Int32 nameID, Int32 width, Int32 height)
UnityEngine.Rendering.CommandBuffer :: Void GetTemporaryRT(Int32 nameID, Int32 width, Int32 height, Int32 depthBuffer)
UnityEngine.Rendering.CommandBuffer :: Void GetTemporaryRT(Int32 nameID, Int32 width, Int32 height, Int32 depthBuffer, FilterMode filter)
UnityEngine.Rendering.CommandBuffer :: Void GetTemporaryRT(Int32 nameID, Int32 width, Int32 height, Int32 depthBuffer, FilterMode filter, RenderTextureFormat format)
UnityEngine.Rendering.CommandBuffer :: Void IssuePluginEvent(IntPtr callback, Int32 eventID)
UnityEngine.Rendering.CommandBuffer :: Void IssuePluginEventAndData(IntPtr callback, Int32 eventID, IntPtr data)
UnityEngine.Rendering.CommandBuffer :: Void IssuePluginEventAndDataWithFlags(IntPtr callback, Int32 eventID, CustomMarkerCallbackFlags flags, IntPtr data)
UnityEngine.Rendering.CommandBuffer :: Void ReleaseTemporaryRT(Int32 nameID)
UnityEngine.Rendering.CommandBuffer :: Void SetBufferData(GraphicsBuffer buffer, NativeArray`1 data, Int32 nativeBufferStartIndex, Int32 graphicsBufferStartIndex, Int32 count)
UnityEngine.Rendering.CommandBuffer :: Void SetComputeIntParam(ComputeShader computeShader, Int32 nameID, Int32 val)
UnityEngine.Rendering.CommandBuffer :: Void SetExecutionFlags(CommandBufferExecutionFlags flags)
UnityEngine.Rendering.CommandBuffer :: Void SetGlobalTexture(Int32 nameID, RenderTargetIdentifier value)
UnityEngine.Rendering.CommandBuffer :: Void SetGlobalTexture(String name, RenderTargetIdentifier value)
UnityEngine.Rendering.CommandBuffer :: Void SetRenderTarget(RenderTargetIdentifier rt)
UnityEngine.Rendering.CommandBuffer :: Void SetRenderTarget(RenderTargetIdentifier rt, RenderBufferLoadAction colorLoadAction, RenderBufferStoreAction colorStoreAction, RenderBufferLoadAction depthLoadAction, RenderBufferStoreAction depthStoreAction)
UnityEngine.Rendering.CommandBuffer :: Void SetViewport(Rect pixelRect)
UnityEngine.Rendering.CommandBuffer :: Void SetViewProjectionMatrices(Matrix4x4 view, Matrix4x4 proj)
UnityEngine.RenderTexture :: Void DiscardContents()
UnityEngine.RenderTexture :: Void DiscardContents(Boolean discardColor, Boolean discardDepth)
UnityEngine.RenderTexture :: IntPtr GetNativeDepthBufferPtr()
UnityEngine.Resources :: static T GetBuiltinResource(String path)
UnityEngine.Resources :: static Object GetBuiltinResource(Type type, String path)
UnityEngine.RuntimeAnimatorController :: AnimationClip[] get_animationClips()
UnityEngine.SceneManagement.SceneManager :: static Int32 get_sceneCount()
UnityEngine.SceneManagement.SceneManager :: static Scene GetSceneAt(Int32 index)
UnityEngine.SceneManagement.SceneManager :: static Void LoadScene(String sceneName)
UnityEngine.SceneManagement.SceneManager :: static Void LoadScene(Int32 sceneBuildIndex)
UnityEngine.SceneManagement.SceneManager :: static AsyncOperation LoadSceneAsync(String sceneName)
UnityEngine.SceneManagement.SceneManager :: static AsyncOperation LoadSceneAsync(Int32 sceneBuildIndex)
UnityEngine.ScreenCapture :: static Void CaptureScreenshot(String filename)
UnityEngine.ScreenCapture :: static Void CaptureScreenshot(String filename, Int32 superSize)
UnityEngine.ScreenCapture :: static Void CaptureScreenshot(String filename, StereoScreenCaptureMode stereoCaptureMode)
UnityEngine.ScreenCapture :: static Void CaptureScreenshot(String filename, Int32 superSize, StereoScreenCaptureMode stereoCaptureMode)
UnityEngine.ScreenCapture :: static Void WarnIfSuperSized(Int32 superSize)
UnityEngine.Scripting.GarbageCollector :: static Boolean CollectIncremental(UInt64 nanoseconds)
UnityEngine.Shader :: static Texture GetGlobalTexture(String name)
UnityEngine.Shader :: static Texture GetGlobalTexture(Int32 nameID)
UnityEngine.Shader :: String GetPropertyName(Int32 propertyIndex)
UnityEngine.Shader :: Vector2 GetPropertyRangeLimits(Int32 propertyIndex)
UnityEngine.Shader :: ShaderPropertyType GetPropertyType(Int32 propertyIndex)
UnityEngine.SkinnedMeshRenderer :: GraphicsBuffer GetPreviousVertexBuffer()
UnityEngine.SkinnedMeshRenderer :: GraphicsBuffer GetVertexBuffer()
UnityEngine.SkinnedMeshRenderer :: Void SetBlendShapeWeight(Int32 index, Single value)
UnityEngine.TestTools.LogAssert :: static Void Expect(LogType type, String message)
UnityEngine.TestTools.LogAssert :: static Void Expect(LogType type, Regex message)
UnityEngine.TestTools.LogAssert :: static Void NoUnexpectedReceived()
UnityEngine.TextCore.LowLevel.FontEngine :: static FontEngineError SetFaceSize(Int32 pointSize)
UnityEngine.TextCore.LowLevel.FontEngine :: static Boolean TryGetGlyphIndex(UInt32 unicode, UInt32& glyphIndex)
UnityEngine.TextCore.LowLevel.FontEngine :: static Boolean TryGetGlyphWithIndexValue(UInt32 glyphIndex, GlyphLoadFlags flags, Glyph& glyph)
UnityEngine.TextCore.LowLevel.FontEngine :: static Boolean TryGetGlyphWithUnicodeValue(UInt32 unicode, GlyphLoadFlags flags, Glyph& glyph)
UnityEngine.Texture2D :: Rect[] PackTextures(Texture2D[] textures, Int32 padding, Int32 maximumAtlasSize, Boolean makeNoLongerReadable)
UnityEngine.Texture2D :: Void SetPixelData(NativeArray`1 data, Int32 mipLevel, Int32 sourceDataStartIndex)
UnityEngine.Texture2D :: Void SetPixelData(T[] data, Int32 mipLevel, Int32 sourceDataStartIndex)
UnityEngine.Texture2D :: Void SetPixelData(ReadOnlySpan`1 bytes, Int32 mipLevel)
UnityEngine.Texture2DArray :: Void Apply()
UnityEngine.Texture2DArray :: Void Apply(Boolean updateMipmaps)
UnityEngine.Texture2DArray :: Void Apply(Boolean updateMipmaps, Boolean makeNoLongerReadable)
UnityEngine.Texture3D :: Void SetPixelData(T[] data, Int32 mipLevel, Int32 sourceDataStartIndex)
UnityEngine.Time :: static Void set_timeScale(Single value)
UnityEngine.Touch :: Int32 get_fingerId()
UnityEngine.Touch :: TouchPhase get_phase()
UnityEngine.Touch :: Vector2 get_position()
UnityEngine.TouchScreenKeyboard :: static Boolean get_isSupported()
UnityEngine.TouchScreenKeyboard :: Status get_status()
UnityEngine.TouchScreenKeyboard :: String get_text()
UnityEngine.TouchScreenKeyboard :: static TouchScreenKeyboard Open(String text, TouchScreenKeyboardType keyboardType, Boolean autocorrection, Boolean multiline, Boolean secure, Boolean alert, String textPlaceholder, Int32 characterLimit)
UnityEngine.TouchScreenKeyboard :: Void set_active(Boolean value)
UnityEngine.TrailRenderer :: Void BakeMesh(Mesh mesh, Boolean useTransform)
UnityEngine.TrailRenderer :: Void BakeMesh(Mesh mesh, Camera camera, Boolean useTransform)
UnityEngine.UI.Graphic :: RectTransform get_rectTransform()
UnityEngine.UI.Graphic :: Void GraphicUpdateComplete()
UnityEngine.UI.Graphic :: Void LayoutComplete()
UnityEngine.UI.Graphic :: Void Rebuild(CanvasUpdate update)
UnityEngine.UI.Image :: Void SetNativeSize()
UnityEngine.UI.MaskableGraphic :: Void Cull(Rect clipRect, Boolean validRect)
UnityEngine.UI.MaskableGraphic :: Material GetModifiedMaterial(Material baseMaterial)
UnityEngine.UI.MaskableGraphic :: Void RecalculateClipping()
UnityEngine.UI.MaskableGraphic :: Void RecalculateMasking()
UnityEngine.UI.MaskableGraphic :: Void SetClipRect(Rect clipRect, Boolean validRect)
UnityEngine.UI.MaskableGraphic :: Void SetClipSoftness(Vector2 clipSoftness)
UnityEngine.Video.VideoPlayer :: Void EnableAudioTrack(UInt16 trackIndex, Boolean enabled)
UnityEngine.Video.VideoPlayer :: Void set_audioOutputMode(VideoAudioOutputMode value)
UnityEngine.Video.VideoPlayer :: Void SetDirectAudioMute(UInt16 trackIndex, Boolean mute)
UnityEngine.Video.VideoPlayer :: Void SetDirectAudioVolume(UInt16 trackIndex, Single volume)
UnityEngine.Video.VideoPlayer :: Void SetTargetAudioSource(UInt16 trackIndex, AudioSource source)
UnityStandardAssets.ImageEffects.PostEffectsBase :: Void DrawBorder(RenderTexture dest, Material material)
UnityStubs.Internal.AssetBundleReader :: static Void ReadParticleSystem(AssetTypeValueField f, ParticleSystem ps)
```

## 用法

1. **先查清单再写代码**：要用某个 Unity API 前，在本附录里搜一下类型名；命中就意味着"能编过、但运行时不生效"。
2. **stub 不会崩**：它只写一条警告日志（查找关键字 `LogStub` / `Waylith`），然后把返回值给成 `default` —— 因此现象往往是"我的效果没出现"，而不是报错。
3. **替代路线**：性能计时改 `Waylith.Profiling.*`；渲染/纹理处理改纯 CPU 路径（`Color[]` + `GetPixelBilinear` + `SetPixels`）；剔除用自己维护的距离判断替代 `CullingGroup`。
4. **注意命名空间**：清单里的类型名是按元数据里 `Namespace.Name` 原样输出的，例如 `UnityEngine.Rendering.CommandBuffer`、`UnityEngine.Profiling.Profiler`、`Unity.Profiling.ProfilerRecorder`（后两者命名空间不同，别混）。

## 复现方式

- 提取脚本：`docs/_stub_scan.ps1`（以 `LogStub` 的 MetadataToken 100663905 = 小端字节 97,2,0,6 为模式扫描每个方法体）
- 原始数据：`docs/unitystubs-stubs.txt`（254 行）、`docs/unitystubs-stub-signatures.txt`（288 行）
- 类型/成员全量快照：`docs/csharp-api.json`（含 Assembly-CSharp / UnityStubs / 0Harmony 三份元数据）
- **坑**：含 IL 字节扫描循环的 .ps1 会被 Defender/AMSI 判定为恶意脚本并拦截（"This script contains malicious content..."），随后该文件不可读也不可运行；需用纯反射脚本重做，或直接复用上面已生成的原始数据。
